![image](assets/logo.png)

![Python Version](https://img.shields.io/badge/python-3.8+-aff.svg)
![OS](https://img.shields.io/badge/os-windows%20|%20linux%20|%20macOS-blue)
![Lisence](https://img.shields.io/badge/license-Apache%202-dfd.svg)
[![PyPI](https://img.shields.io/pypi/v/docapi)](https://pypi.org/project/docapi/)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/Shulin-Zhang/docapi/pulls)

\[ 中文 | [English](README.md) \]

DocAPI 是一个使用 LLM 自动生成 API 文档的 Python 包，支持 Flask 和 Django。

## 注意

1.x.x版本相对于0.x.x使用方式发生了变化，请参照下面使用方式。

## 特性

- 对于Flask框架支持自动扫描API服务的路由结构；
  
- 支持多种国内外主流商业和开源模型；
  
- 支持自动生成文档和局部更新文档；

- 支持多种语言的API文档（需要大模型支持）；

- 支持web页面部署展示API文档。

## 更新日志

- [2024-11-17] 支持智谱AI，百度千帆模型，优化文档结构，增加javascript代码示例；去除使用配置文件的执行方式。

- [2024-11-20] 支持自定义文档模版。

- [2024-11-24] 支持多线程加速请求。

- [2024-11-26] 支持.env加载环境变量和多国语言文档。

- [2024-12-02] windows操作系统测试通过 (需要使用power shell 或 windows terminal)；新的模型名称提供方式，防止环境变量冲突 (参照下面使用方法)。

## 安装

```bash
pip install -U docapi
```

#### pypi官方源安装

```bash
pip install -U docapi -i https://pypi.org/simple
```

#### github源码安装

```bash
pip install git+https://github.com/Shulin-Zhang/docapi
```

## 使用方法

**docapi建立更新文档需要使用API服务项目环境。**

**OpenAI:**
```bash
export DOCAPI_MODEL=openai:gpt-4o-mini

export OPENAI_API_KEY=api_key

# 生成文档
docapi generate server.py

# 更新文档
docapi update server.py

# 启动web服务
docapi serve
```

**Azure OpenAI:**
```bash
export DOCAPI_MODEL=azure-openai:gpt-4o-mini

export AZURE_OPENAI_API_KEY=api_key

export AZURE_OPENAI_ENDPOINT=endpoint

export OPENAI_API_VERSION=version

# 生成文档
docapi generate server.py --template <template_path>

# 更新文档
docapi update server.py --template <template_path>

# 启动web服务
docapi serve docs --ip 0.0.0.0 --port 9000
```

**开源模型:**
```bash
export DOCAPI_MODEL=open-source:model_name

export OPENAI_API_KEY=api_key

export OPENAI_API_BASE=api_base_url

# 生成文档
docapi generate server.py

# 更新文档
docapi update server.py

# 启动web服务
docapi serve
```

**百度千帆:**
```bash
export DOCAPI_MODEL=baidu:ERNIE-4.0-Turbo-8K

export QIANFAN_ACCESS_KEY=access_key

export QIANFAN_SECRET_KEY=secret_key

# 生成文档
docapi generate server.py

# 更新文档
docapi update server.py

# 启动web服务
docapi serve
```

**通义千问:**
```bash
export DOCAPI_MODEL=aliyun:qwen-turbo

export OPENAI_API_KEY=api_key

# 生成文档
docapi generate server.py --workers 6

# 更新文档
docapi update server.py --workers 6

# 启动web服务
docapi serve
```

**智谱AI:**
```bash
export DOCAPI_MODEL=zhipu:glm-4-flash

export ZHIPUAI_API_KEY=api_key

# 生成文档
docapi generate server.py

# 更新文档
docapi update server.py

# 启动web服务
docapi serve
```

**.env环境变量文件:**

```.env
# .env
DOCAPI_MODEL = openai:gpt-4o-mini

OPENAI_API_KEY = 'you-api-key'
```

```bash
# 生成文档
docapi generate server.py --env .env
```

## 代码调用
```python
import os
from docapi import DocAPI

os.environ['OPENAI_API_KEY'] = "api_key"

docapi = DocAPI.build(lang="zh", model="openai:gpt-4o-mini")

docapi.generate("flask_project/server.py", "docs")

# docapi.update("flask_project/server.py", "docs")

# docapi.serve("docs", ip="127.0.0.1", port=8080)
```

## 支持模型

- OpenAI

- AzureOpenAI

- XAI

- 开源模型

- 百度千帆

- 通义千问

- 智谱AI

## 支持API框架

- Flask
  
## API Web页面

![image](assets/example1.png)

## TODO

- ~~支持文心一言、智谱AI等大模型。~~

- ~~支持文档在线web页面展示。~~

- ~~支持自定义文档模版。~~

- ~~多线程加速请求。~~

- ~~支持Windows操作系统.~~

- 支持django框架。

- 大模型封装采用`aisuite`。

- 导入到postman。
