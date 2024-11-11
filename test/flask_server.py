import inspect
from flask import Flask, request, jsonify
from sub_api import sub_api

app = Flask(__name__)
app.register_blueprint(sub_api, url_prefix='/sub_api')


# 定义路由和视图函数
@app.route('/users', methods=['GET'])
def get_users():
    return "List of users"

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    '''hello world'''
    return f"User {user_id}"

# 创建学生系统用户
@app.route('/users/create', methods=['POST'])
def create_user():
    params = request.get_json()
    name = params['name']
    age = params['age']
    data = {'name': name, 'age': age}

    return jsonify(code=0, data=data, error=None)

# 解析 Flask 路由结构
def extract_routes(app):
    routes = []
    for rule in app.url_map.iter_rules():
        # print(dir(rule))
        view_func = app.view_functions[rule.endpoint]
        route_info = {
            "endpoint": rule.endpoint,
            "url": rule.rule,
            "path": inspect.getfile(view_func),
            "methods": list(rule.methods - {'HEAD', 'OPTIONS'}),
        }
        routes.append(route_info)
    return routes

# # 输出解析结果
# for route in extract_routes(app):
#     print(f"Endpoint: {route['endpoint']}")
#     print(f"URL: {route['url']}")
#     print(f"Methods: {route['methods']}")
#     print(f'Path: {route["path"]}')
#     print("-" * 40)
