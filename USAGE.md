# 使用方法

**注意**：`docapi` 工具需要在相应的 API 服务环境下运行，以生成和更新文档。

---

## 使用环境变量

### OpenAI 示例
```bash
export DOCAPI_MODEL=openai:gpt-4o-mini
export OPENAI_API_KEY=your_api_key

# 为 Flask 框架生成文档
docapi generate server.py

# 为 Django 框架生成文档
# docapi generate manage.py

# 更新 Flask 框架的文档
docapi update server.py

# 更新 Django 框架的文档
# docapi update manage.py

# 启动文档展示的 Web 服务
docapi serve
```

### Azure OpenAI 示例
```bash
export DOCAPI_MODEL=azure-openai:gpt-4o-mini
export AZURE_OPENAI_API_KEY=your_api_key
export AZURE_OPENAI_ENDPOINT=your_endpoint
export OPENAI_API_VERSION=api_version

# 使用自定义模板生成文档
docapi generate server.py --template <template_path>

# 使用自定义模板更新文档
docapi update server.py --template <template_path>

# 启动 Web 服务，指定自定义 IP 和端口
docapi serve docs --ip 0.0.0.0 --port 9000
```

### XAI 示例
```bash
export DOCAPI_MODEL=xai:grok-beta
export XAI_API_KEY=your_api_key

# 生成文档
docapi generate manage.py

# 更新文档
docapi update manage.py

# 启动 Web 服务
docapi serve
```

### 开源模型示例
```bash
export DOCAPI_MODEL=open-source:model_name
export OPENAI_API_KEY=your_api_key
export OPENAI_API_BASE=api_base_url

# 生成文档
docapi generate server.py

# 更新文档
docapi update server.py

# 启动 Web 服务
docapi serve
```

### 百度千帆示例
```bash
export DOCAPI_MODEL=baidu:ERNIE-4.0-Turbo-8K
export QIANFAN_ACCESS_KEY=your_access_key
export QIANFAN_SECRET_KEY=your_secret_key

# 生成文档
docapi generate server.py

# 更新文档
docapi update server.py

# 启动 Web 服务
docapi serve
```

### 通义千问示例
```bash
export DOCAPI_MODEL=aliyun:qwen-turbo
export DASHSCOPE_API_KEY=your_api_key

# 使用多线程生成文档
docapi generate manage.py --workers 6

# 使用多线程更新文档
docapi update manage.py --workers 6

# 启动 Web 服务
docapi serve
```

### 智谱 AI 示例
```bash
export DOCAPI_MODEL=zhipu:glm-4-flash
export ZHIPUAI_API_KEY=your_api_key

# 生成文档
docapi generate server.py

# 更新文档
docapi update server.py

# 启动 Web 服务
docapi serve
```

---

## 使用环境变量配置文件

可以通过配置 `.env` 文件来管理环境变量：

```.env
DOCAPI_MODEL=openai:gpt-4o-mini
OPENAI_API_KEY=your_api_key
```

使用 `.env` 文件运行命令：
```bash
# 生成文档
docapi generate server.py --env .env

# 更新文档
docapi update server.py --env .env

# 启动 Web 服务
docapi serve
```

使用具体模型和自定义配置的示例：
```bash
# 生成文档
docapi generate server.py docs --env .env --model aliyun:qwen-turbo

# 更新文档
docapi update server.py docs --env .env --model aliyun:qwen-turbo

# 启动 Web 服务，指定 IP 和端口
docapi serve docs --ip 0.0.0.0 --port 9000
```

---

## 使用代码
```python
import os
from docapi import DocAPI

# 配置 API 密钥
os.environ['OPENAI_API_KEY'] = "your_api_key"

# 使用指定模型初始化 DocAPI
docapi = DocAPI.build(lang="zh", model="openai:gpt-4o-mini")

# 生成文档
docapi.generate("flask_project/server.py", "docs")

# 更新文档
# docapi.update("flask_project/server.py", "docs")

# 本地启动文档服务
# docapi.serve("docs", ip="127.0.0.1", port=8080)
```
