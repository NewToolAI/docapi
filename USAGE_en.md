# Usage

**Note:** The `docapi` tool requires the appropriate API service environment to generate and update documentation.  

---

## Using Environment Variables

### OpenAI Example
```bash
export DOCAPI_MODEL=openai:gpt-4o-mini
export OPENAI_API_KEY=your_api_key

# Generate documentation for Flask
docapi generate server.py

# Generate documentation for Django
# docapi generate manage.py

# Update documentation for Flask
docapi update server.py

# Update documentation for Django
# docapi update manage.py

# Launch the web server to display the documentation
docapi serve
```

### Azure OpenAI Example
```bash
export DOCAPI_MODEL=azure-openai:gpt-4o-mini
export AZURE_OPENAI_API_KEY=your_api_key
export AZURE_OPENAI_ENDPOINT=your_endpoint
export OPENAI_API_VERSION=api_version

# Generate documentation with a custom template
docapi generate server.py --template <template_path>

# Update documentation with a custom template
docapi update server.py --template <template_path>

# Launch the web service on a custom IP and port
docapi serve docs --ip 0.0.0.0 --port 9000
```

### XAI Example
```bash
export DOCAPI_MODEL=xai:grok-beta
export XAI_API_KEY=your_api_key

# Generate documentation
docapi generate manage.py

# Update documentation
docapi update manage.py

# Launch the web service
docapi serve
```

### Open-Source Models Example
```bash
export DOCAPI_MODEL=open-source:model_name
export OPENAI_API_KEY=your_api_key
export OPENAI_API_BASE=api_base_url

# Generate documentation
docapi generate server.py

# Update documentation
docapi update server.py

# Launch the web service
docapi serve
```

### Baidu Qianfan Example
```bash
export DOCAPI_MODEL=baidu:ERNIE-4.0-Turbo-8K
export QIANFAN_ACCESS_KEY=your_access_key
export QIANFAN_SECRET_KEY=your_secret_key

# Generate documentation
docapi generate server.py

# Update documentation
docapi update server.py

# Launch the web service
docapi serve
```

### Tongyi Qianwen Example
```bash
export DOCAPI_MODEL=aliyun:qwen-turbo
export DASHSCOPE_API_KEY=your_api_key

# Generate documentation with parallel processing
docapi generate manage.py --workers 6

# Update documentation with parallel processing
docapi update manage.py --workers 6

# Launch the web service
docapi serve
```

### Zhipu AI Example
```bash
export DOCAPI_MODEL=zhipu:glm-4-flash
export ZHIPUAI_API_KEY=your_api_key

# Generate documentation
docapi generate server.py

# Update documentation
docapi update server.py

# Launch the web service
docapi serve
```

---

## Using Environment Variable Configuration Files

To use a configuration file, create and edit a `.env` file:
```.env
DOCAPI_MODEL=openai:gpt-4o-mini
OPENAI_API_KEY=your_api_key
```

Run commands with the `.env` file:
```bash
# Generate documentation
docapi generate server.py --env .env

# Update documentation
docapi update server.py --env .env

# Launch the web service
docapi serve
```

Example with a specific model and custom settings:
```bash
# Generate documentation
docapi generate server.py docs --env .env --model aliyun:qwen-turbo

# Update documentation
docapi update server.py docs --env .env --model aliyun:qwen-turbo

# Launch the web service on a specific IP and port
docapi serve docs --ip 0.0.0.0 --port 9000
```

---

## Using Code Directly
```python
import os
from docapi import DocAPI

# Configure API key
os.environ['OPENAI_API_KEY'] = "your_api_key"

# Initialize DocAPI with a specific model
docapi = DocAPI.build(lang="zh", model="openai:gpt-4o-mini")

# Generate documentation
docapi.generate("flask_project/server.py", "docs")

# Update documentation (uncomment to use)
# docapi.update("flask_project/server.py", "docs")

# Serve documentation locally
# docapi.serve("docs", ip="127.0.0.1", port=8080)
```
