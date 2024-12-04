# 使用方法 (Usage)

**注意：docapi建立更新文档需要使用API服务项目环境。**

**Note: The docapi tool requires the API service project environment to generate and update documentation.**

## 使用环境变量 (Use environment variables)

**OpenAI:**
```bash
export DOCAPI_MODEL=openai:gpt-4o-mini

export OPENAI_API_KEY=api_key

# Generate documentation
docapi generate server.py

# Update documentation
docapi update server.py

# Start the web service
docapi serve
```

**Azure OpenAI:**
```bash
export DOCAPI_MODEL=azure-openai:gpt-4o-mini

export AZURE_OPENAI_API_KEY=api_key

export AZURE_OPENAI_ENDPOINT=endpoint

export OPENAI_API_VERSION=version

# Generate documentation
docapi generate server.py --template <template_path>

# Update documentation
docapi update server.py --template <template_path>

# Start the web service
docapi serve docs --ip 0.0.0.0 --port 9000
```

**XAI:**
```bash
export DOCAPI_MODEL=xai:grok-beta

export XAI_API_KEY=api_key

# Generate documentation
docapi generate server.py

# Update documentation
docapi update server.py

# Start the web service
docapi serve
```

**Open-Source Models:**
```bash
export DOCAPI_MODEL=open-source:model_name

export OPENAI_API_KEY=api_key

export OPENAI_API_BASE=api_base_url

# Generate documentation
docapi generate server.py

# Update documentation
docapi update server.py

# Start the web service
docapi serve
```

**Baidu Qianfan:**
```bash
export DOCAPI_MODEL=baidu:ERNIE-4.0-Turbo-8K

export QIANFAN_ACCESS_KEY=access_key

export QIANFAN_SECRET_KEY=secret_key

# Generate documentation
docapi generate server.py

# Update documentation
docapi update server.py

# Start the web service
docapi serve
```

**Tongyi Qianwen:**
```bash
export DOCAPI_MODEL=aliyun:qwen-turbo

export DASHSCOPE_API_KEY=api_key

# Generate documentation
docapi generate server.py --workers 6

# Update documentation
docapi update server.py --workers 6

# Start the web service
docapi serve
```

**Zhipu AI:**
```bash
export DOCAPI_MODEL=zhipu:glm-4-flash

export ZHIPUAI_API_KEY=api_key

# Generate documentation
docapi generate server.py

# Update documentation
docapi update server.py

# Start the web service
docapi serve
```

##  使用环境变量配置文件 (Use environment variable configuration files)

Edit the environment variable file (编辑环境变量文件):
```.env
# .env
DOCAPI_MODEL = openai:gpt-4o-mini

OPENAI_API_KEY = 'your-api-key'

DASHSCOPE_API_KEY = 'your-api-key'
```

```bash
# Generate documentation
docapi generate server.py --env .env

# Update documentation
docapi update server.py --env.env

# Start the web service
docapi serve
```

```bash
docapi generate server.py docs --env .env --model aliyun:qwen-turbo

docapi update server.py docs --env .env --model aliyun:qwen-turbo

docapi serve docs --ip 0.0.0.0 --port 9000
```

## 使用代码 (Use Code)
```python
import os
from docapi import DocAPI

os.environ['OPENAI_API_KEY'] = "api_key"

docapi = DocAPI.build(lang="zh", model="openai:gpt-4o-mini")

docapi.generate("flask_project/server.py", "docs")

# docapi.update("flask_project/server.py", "docs")

# docapi.serve("docs", ip="127.0.0.1", port=8080)
```
