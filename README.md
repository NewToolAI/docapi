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
**Note: You must be in the environment of your API project when using docapi.**

#### Method 1

```bash
export OPENAI_API_KEY=your_key

# Generate API documentation
docapi generate server.py

# Update API documentation
docapi update server.py

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
openai_api_key: xxx

openai_base_url: 'http://ip:port/v1'

openai_model: 'qwen-plus'
```

```bash
# Generate API documentation
docapi generate server.py ./docs --lang zh --config config.yaml

# Update API documentation
docapi update server.py ./docs --lang zh --config config.yaml

# Start the web service
docapi serve ./docs -h 127.0.0.1 -p 9000
```

## Supported Models
- OpenAI
- AzureOpenAI
- Tongyi Qianwen

## Supported API Frameworks
- Flask

## TODO
- Support models like Wenxin Yiyan, Zhipu AI, etc.
- Support frameworks like FastAPI, Django, etc.
~~- Support online web page display of documentation~~
- Support custom documentation templates
- Multi-threaded request acceleration
- Import to Postman
