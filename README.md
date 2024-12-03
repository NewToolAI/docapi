![image](assets/logo.png)

![Python Version](https://img.shields.io/badge/python-3.8+-aff.svg)
![OS](https://img.shields.io/badge/os-windows%20|%20linux%20|%20macOS-blue)
![License](https://img.shields.io/badge/license-Apache%202-dfd.svg)
[![PyPI](https://img.shields.io/pypi/v/docapi)](https://pypi.org/project/docapi/)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/Shulin-Zhang/docapi/pulls)

\[ [中文](README_zh.md) | English \]

DocAPI is a Python package that leverages LLMs to automatically generate API documentation, supporting both Flask and Django frameworks.

## Notice

The usage of version 1.x.x has changed compared to 0.x.x. Please refer to the instructions below for details.

## Features

- Automatic scanning of API service routes for the Flask framework;
  
- Support for various mainstream commercial and open-source models, both domestic and international;
  
- Automatic documentation generation and partial updates;

- Multi-language API documentation generation (requires large model support);

- Web page deployment for API documentation display.

## Changelog

- **[2024-11-17]** Added support for Zhipu AI and Baidu Qianfan models, optimized documentation structure, included JavaScript code examples; removed the execution method using configuration files.

- **[2024-11-20]** Added support for custom documentation templates.

- **[2024-11-24]** Enabled multi-threading for accelerated requests.

- **[2024-11-26]** Added support for .env files to load environment variables and multi-language documentation.

- **[2024-12-02]** Successfully tested on Windows OS (requires PowerShell or Windows Terminal); introduced a new way of specifying model names to prevent environment variable conflicts (see usage instructions below).

## Installation

```bash
pip install -U docapi
```

#### Install from PyPI Official Repository

```bash
pip install -U docapi -i https://pypi.org/simple
```

#### Install from GitHub Source

```bash
pip install git+https://github.com/Shulin-Zhang/docapi
```

## Usage

**docapi requires the API service project environment to create or update documentation.**

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

export OPENAI_API_KEY=api_key

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

**Using .env Environment Variable File:**

```.env
# .env
DOCAPI_MODEL = openai:gpt-4o-mini

OPENAI_API_KEY = 'your-api-key'
```

```bash
# Generate documentation
docapi generate server.py --env .env
```

## Code Usage
```python
import os
from docapi import DocAPI

os.environ['OPENAI_API_KEY'] = "api_key"

docapi = DocAPI.build(lang="zh", model="openai:gpt-4o-mini")

docapi.generate("flask_project/server.py", "docs")

# docapi.update("flask_project/server.py", "docs")

# docapi.serve("docs", ip="127.0.0.1", port=8080)
```

## Supported Models

- OpenAI

- Azure OpenAI

- XAI

- Open-Source Models

- Baidu Qianfan

- Tongyi Qianwen

- Zhipu AI

## Supported API Frameworks

- Flask
  
## API Web Page

![image](assets/example1.png)

## TODO

- ~~Support large models like Wenxin Yiyan and Zhipu AI.~~

- ~~Enable online web page documentation display.~~

- ~~Add support for custom documentation templates.~~

- ~~Implement multi-threading for accelerated requests.~~

- ~~Support Windows OS.~~

- Add support for Django framework.

- Use `aisuite` for large model encapsulation.

- Enable export to Postman.

