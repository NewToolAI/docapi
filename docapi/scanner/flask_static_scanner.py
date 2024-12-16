import ast
import hashlib
from pathlib import Path
from typing import List, Dict, Any

from docapi.scanner.base_scanner import BaseScanner


class FlaskStaticScanner(BaseScanner):

    def scan(self, app_path: str) -> Dict[str, Any]:
        app_dir = Path(app_path).parent
        structures = {}

        # Recursively scan all Python files in the provided directory
        for file_path in app_dir.rglob("*.py"):
            file_path_str = str(file_path.resolve())  # Convert file_path to string once
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    source_code = f.read()  # Read the file content

                tree = ast.parse(source_code)  # Parse the file into an AST
                self._add_parents(tree)  # Add parent references for traversal
                routes = self._scan_flask_routes(tree, file_path_str)

                if routes:
                    if file_path_str not in structures:
                        structures[file_path_str] = []
                    structures[file_path_str].extend(routes)  # Store routes by file

            except Exception as e:
                print(f"Error scanning {file_path}: {e}")  # Handle errors gracefully

        structures = self._sort_structures(structures)  # Sort routes for better readability
        return structures

    def _scan_flask_routes(self, tree: ast.AST, file_path: str) -> List[Dict[str, Any]]:
        routes = []

        # Traverse all nodes in the AST to identify Flask routes
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):  # Look for function calls
                # Ensure the function call is specifically a Flask route
                if (
                    isinstance(node.func, ast.Attribute) and  # Ensure the call is an attribute (e.g., app.route)
                    node.func.attr == "route" and  # Ensure the attribute is "route"
                    isinstance(node.func.value, ast.Name) and  # Ensure the call object is a variable or name
                    len(node.args) >= 1 and  # Ensure there is at least one argument
                    isinstance(node.args[0], ast.Constant) and  # Ensure the first argument is a constant
                    isinstance(node.args[0].value, str)  # Ensure the constant is a string (route URL)
                ):
                    route_path = node.args[0].value  # Extract the route URL

                    # Retrieve the parent function node to determine the associated view function
                    function_node = self._get_parent_function(node)
                    if function_node:
                        comments = ast.get_docstring(function_node)  # Extract the docstring if available
                        try:
                            function_code = ast.unparse(function_node)  # Get the function source code
                        except Exception:
                            function_code = "<unparsable>"  # Handle unparsable code gracefully
                        code = ("# " + comments + "\n" + function_code).strip() if comments else function_code  # Combine comments and code
                    else:
                        code = "<unknown>"

                    # Append route details to the list
                    routes.append({
                        "url": route_path,
                        "code": code,
                        "md5": self._generate_md5(code),  # Generate MD5 hash of the code for tracking
                    })

        return routes

    def _get_parent_function(self, node: ast.AST) -> ast.FunctionDef:
        # Traverse upwards in the AST to find the parent function node
        while node:
            node = getattr(node, "parent", None)
            if isinstance(node, ast.FunctionDef):
                return node
        return None

    def _add_parents(self, tree: ast.AST):
        # Add parent references to child nodes for easier traversal
        for node in ast.walk(tree):
            for child in ast.iter_child_nodes(node):
                child.parent = node

    def _generate_md5(self, content: str) -> str:
        # Generate an MD5 hash for the given content
        return hashlib.md5(content.encode("utf-8")).hexdigest()

    def _sort_structures(self, structures: Dict[str, List[Dict[str, Any]]]) -> Dict[str, List[Dict[str, Any]]]:
        # Sort routes by URL within each file
        new_structures = {}
        for path, item_list in structures.items():
            new_structures[path] = sorted(item_list, key=lambda x: x["url"])
        return new_structures


# test
if __name__ == "__main__":
    import json

    project_dir = "../../test/django_project"
    scanner = FlaskStaticScanner()  # Initialize the Flask scanner
    result = scanner.scan(project_dir)  # Perform the scan

    print(json.dumps(result, indent=4, ensure_ascii=False))  # Output the results in JSON format
