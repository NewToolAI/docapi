![image](assets/logo.png)

![Python Version](https://img.shields.io/badge/python-3.8+-aff.svg)
![Lisence](https://img.shields.io/badge/license-Apache%202-dfd.svg)
[![PyPI](https://img.shields.io/pypi/v/docapi)](https://pypi.org/project/docapi/)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/Shulin-Zhang/docapi/pulls)

\[ English | [中文](README_zh.md) \]

#### DocAPI is a Python package that automatically generates API documentation using large models. It scans the API route structure, generates or updates the documentation, and provides code call examples.

## Installation

```bash
pip install docapi

or

pip install -U docapi -i https://pypi.org/simple
```

#### GitHub source code installation

```bash
pip install git+https://github.com/Shulin-Zhang/docapi
```

## Usage

**auto_scan is only valid for flask projects and must be used in the environment of api projects.**

#### Method 1

```bash
export OPENAI_API_KEY=your_key

# Generate API documentation
docapi generate server.py --auto_scan

# Update API documentation
docapi update server.py --auto_scan

# Start the web service
docapi serve
```

#### Method 2

Generate the configuration file

```bash
docapi init
```

Edit the config.yaml file

```yaml
# API file list

api_files: 
  - 'flask_server.py'
  - 'flask_api.py'

# OpenAI

openai_api_key: xxx

openai_base_url: 'http://ip:port/v1'

openai_model: 'qwen-plus'

# Azure OpenAI

azure_api_key: null

azure_endpoint: null

azure_api_version: null

azure_model: null
```

```bash
# Generate API documentation
docapi generate --doc_dir ./docs --lang zh --config config.yaml

# Update API documentation
docapi update --doc_dir ./docs --lang zh --config config.yaml

# Start the web service
docapi serve ./docs -h 127.0.0.1 -p 9000
```

## Supported Models

- OpenAI

- AzureOpenAI

- Tongyi Qianwen

## Supported API Frameworks

Manually specifying the API file list is valid for any API framework. Automatic scanning is only valid for the Flask framework.

## API Web Page

![image](assets/example1.png)

## TODO
- Supports large models such as Wenxin Yiyan and Zhipu AI.

- Supports automatic scanning of frameworks such as fastapi and Django.

- ~~Supports online web page display of documents.~~

- Supports custom document templates.

- Multithreading accelerates requests.

- Import to postman.
