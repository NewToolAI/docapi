![image](assets/logo.png)

![Python Version](https://img.shields.io/badge/python-3.8+-aff.svg)
![OS](https://img.shields.io/badge/os-linux%20|%20macOS-blue)
![Lisence](https://img.shields.io/badge/license-Apache%202-dfd.svg)
[![PyPI](https://img.shields.io/pypi/v/docapi)](https://pypi.org/project/docapi/)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/Shulin-Zhang/docapi/pulls)

\[ 中文 | [English](README.md) \]

DocAPI 是一个使用 LLM 自动生成 API 文档的 Python 包。

## 特性

- 对于Flask框架支持自动扫描API服务的路由结构；
  
- 支持多种国内外主流商业和开源模型；
  
- 支持自动生成文档和局部更新文档；

- 支持中文、英文文档；

- 支持web页面部署展示API文档。

## 安装

```bash
pip install -U docapi
```

或

```bash
pip install -U docapi -i https://pypi.org/simple
```

#### github源码安装

```bash
pip install git+https://github.com/Shulin-Zhang/docapi
```

## 使用方法

**自动扫描路由结构，只对flask项目有效，必须在api项目的环境中使用。**

OpenAI:
```bash
export OPENAI_API_KEY=api_key

export OPENAI_API_MODEL=gpt-4o-mini

# 生成文档
docapi generate server.py

# 更新文档
docapi update server.py

# 启动web服务
docapi serve
```

Azure OpenAI:
```bash
export AZURE_OPENAI_API_KEY=api_key

export AZURE_OPENAI_ENDPOINT=endpoint

export OPENAI_API_VERSION=version

export AZURE_OPENAI_MODEL=gpt-4o-mini

# 生成文档
docapi generate server.py --template <template_path>

# 更新文档
docapi update server.py --template <template_path>

# 启动web服务
docapi serve docs --ip 0.0.0.0 --port 9000
```

千问, 开源模型部署:
```bash
export OPENAI_API_KEY=api_key

export OPENAI_API_BASE=api_base_url

export OPENAI_API_MODEL=model_name

# 生成文档
docapi generate server.py

# 更新文档
docapi update server.py

# 启动web服务
docapi serve
```

百度千帆:
```bash
export QIANFAN_ACCESS_KEY=access_key

export QIANFAN_SECRET_KEY=secret_key

export QIANFAN_MODEL=ERNIE-3.5-8K

# 生成文档
docapi generate server.py

# 更新文档
docapi update server.py

# 启动web服务
docapi serve
```

智谱AI:
```bash
export ZHIPUAI_API_KEY=api_key

export ZHIPUAI_MODEL=glm-4-flash

# 生成文档
docapi generate server.py

# 更新文档
docapi update server.py

# 启动web服务
docapi serve
```

## 代码调用
```python
import os
from docapi import DocAPI, llm_builder, prompt
from docapi.scanner import flask_scanner

os.environ['OPENAI_API_KEY'] = "api_key"
os.environ['OPENAI_API_BASE'] = "api_base"
os.environ['OPENAI_API_MODEL'] = "model_name"

docapi = DocAPI.build(lang="zh")

# template = '''<document template>
# '''

# docapi = DocAPI(llm=llm_builder.build_llm(), scanner=flask_scanner, prompt=prompt.doc_zh, template=template)

docapi.generate("flask_project/flask_server.py", "docs")

# docapi.update("flask_project/flask_server.py", "docs")

# docapi.serve("docs", ip="127.0.0.1", port=8080)
```

## 更新日志

- [2024-11-17] 支持智谱AI，百度千帆模型，优化文档结构，增加javascript代码示例；去除使用配置文件的执行方式。

- [2024-11-20] 支持自定义文档模版。

- [2024-11-24] 支持多线程加速请求。

## 支持模型

- OpenAI

- AzureOpenAI

- 通义千问

- 智谱AI

- 百度千帆

- 开源模型

## 支持API框架

- Flask
  
自动扫描只对Flask框架有效，推荐Flask服务上使用。

## API Web页面

![image](assets/example1.png)

## TODO

- ~~支持文心一言、智谱AI等大模型。~~

- 支持django框架的路由自动扫描。

- ~~支持文档在线web页面展示。~~

- ~~支持自定义文档模版。~~

- ~~多线程加速请求。~~

- 导入到postman。
