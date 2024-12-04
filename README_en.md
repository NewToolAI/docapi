![image](assets/logo.png)

![Python Version](https://img.shields.io/badge/python-3.8+-aff.svg)
![OS](https://img.shields.io/badge/os-windows%20|%20linux%20|%20macOS-blue)
![License](https://img.shields.io/badge/license-Apache%202-dfd.svg)
[![PyPI](https://img.shields.io/pypi/v/docapi)](https://pypi.org/project/docapi/)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/Shulin-Zhang/docapi/pulls)

\[ [中文](README.md) | English \]

DocAPI is a Python package that leverages LLMs to automatically generate API documentation, supporting both Flask and Django frameworks.

## Notice

- The usage of version 1.x.x has changed compared to 0.x.x. Please refer to the instructions below for details.

- The docapi tool requires the API service project environment to generate and update documentation.

## Features

- Supports automatic scanning of API service routing structure.
  
- Supports various mainstream commercial and open-source models, both domestic and international.
  
- Supports automatic generation and partial updates of documentation.
  
- Supports API documentation in multiple languages (requires large model support).
  
- Supports web-based deployment for displaying API documentation.

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

**[More usage methods](USAGE.md)**

## Supported Models

- OpenAI

- Azure OpenAI

- XAI

- Open-Source Models

- Baidu Qianfan

- Tongyi Qianwen

- Zhipu AI

## Supported API Frameworks

- Flask (>=3.0.0)

- Django (>=4.2.0)
  
## API Web Page

![image](assets/example1.png)

## TODO

- ~~Support large models like Wenxin Yiyan and Zhipu AI.~~

- ~~Enable online web page documentation display.~~

- ~~Add support for custom documentation templates.~~

- ~~Implement multi-threading for accelerated requests.~~

- ~~Support Windows OS.~~

- ~~Add support for Django framework.~~

- Enable export to Postman.
