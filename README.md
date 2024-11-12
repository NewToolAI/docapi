![image](assets/logo.png)


![Python Version](https://img.shields.io/badge/python-3.8+-aff.svg)
![Lisence](https://img.shields.io/badge/license-Apache%202-dfd.svg)
[![PyPI](https://img.shields.io/pypi/v/docapi)](https://pypi.org/project/docapi/)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/Shulin-Zhang/docapi/pulls)

\[ English | [中文](README_zh.md) \]

### DocAPI is a Python package that automatically generates API documentation using large models. It scans the API route structure, generates or updates the documentation, and provides code call examples.

## Installation

```bash
pip install docapi

or

pip install docapi -i https://pypi.org/simple
```

## Usage
**Note: You must be in the environment of your API project when using docapi.**

### Method 1

```bash
export OPENAI_API_KEY=your_key

docapi generate server.py

docapi update server.py
```

### Method 2

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
docapi generate server.py ./docs --lang zh --config config.yaml

docapi update server.py ./docs --lang zh --config config.yaml
```

### Supported Models
- OpenAI
- AzureOpenAI
- Tongyi Qianwen

### Supported API Frameworks
- Flask

### TODO
- Support models like Wenxin Yiyan, Zhipu AI, etc.
- Support frameworks like FastAPI, Django, etc.
- Support online web page display of documentation
- Support custom documentation templates
- Multi-threaded request acceleration
- Import to Postman
- :w
- 