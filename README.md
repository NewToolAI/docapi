# ![image](assets/logo.png)

![Python Version](https://img.shields.io/badge/python-3.8+-aff.svg)
![OS](https://img.shields.io/badge/os-windows%20|%20linux%20|%20macos-blue)
![License](https://img.shields.io/badge/license-Apache%202-dfd.svg)
[![PyPI](https://img.shields.io/pypi/v/docapi)](https://pypi.org/project/docapi/)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/Shulin-Zhang/docapi/pulls)

\[ English | [中文](README_zh.md) \]

**DocAPI** is a Python library powered by Large Language Models (LLMs) designed for automatically generating API documentation. It currently supports **Flask** and **Django**, enabling seamless documentation generation and updates to enhance developer productivity.

---

## Important Notes

- **Version 1.x.x** introduces breaking changes compared to **0.x.x**. Please refer to the updated usage guide below.  
- Generating or updating documents requires the dependent environment of the API service.

---

## Key Features

- **Framework Support**: Automatically scans routing structures for Flask and Django applications.  
- **Multi-Model Compatibility**: Works with a wide range of commercial and open-source LLMs.  
- **Documentation Management**: Generates complete documentation or performs incremental updates.  
- **Multi-Language Support**: Creates multilingual API documentation (requires LLM support).  
- **Web Integration**: Supports deploying documentation on a web interface.

---

## Changelog

- [2024-11-17]: Added support for Zhipu AI and Baidu Qianfan models, optimized documentation structure, and introduced JavaScript code examples. Removed configuration file execution mode.  
- [2024-11-20]: Added custom documentation template support.  
- [2024-11-24]: Enabled multithreading for faster request handling.  
- [2024-11-26]: Introduced `.env` file support for environment variables and multi-language documentation.  
- [2024-12-02]: Successfully tested on Windows (requires PowerShell or Windows Terminal). Improved model naming to avoid environment variable conflicts.  
- [2024-12-05]: Fully supports and tested on Django versions 3, 4, and 5.  

---

## Installation

Install the latest version via PyPI:

```bash
pip install -U docapi
```

Install with all dependencies:

```bash
pip install -U "docapi[all]"
```

Install for specific frameworks:

```bash
pip install -U "docapi[flask]"
```

```bash
pip install -U "docapi[django]"
```

**Install from PyPI official source:**

```bash
pip install -U "docapi[all]" -i https://pypi.org/simple
```

**Install from GitHub:**

```bash
pip install git+https://github.com/Shulin-Zhang/docapi
```

---

## Usage Guide

Here are typical usage examples:

### OpenAI Model Example

#### 1. Set up the model and API key:
```bash
export DOCAPI_MODEL=openai:gpt-4o-mini

export OPENAI_API_KEY=your_api_key
```

#### 2. Generate documentation:
- For Flask:
```bash
docapi generate server.py
```
- For Django:
```bash
docapi generate manage.py
```

#### 3. Update documentation:
- For Flask:
```bash
docapi update server.py
```
- For Django:
```bash
docapi update manage.py
```

#### 4. Start a web server to display the documentation:
```bash
docapi serve
```

[Find more usage details in the guide](USAGE_en.md).

---

## Supported Models

- OpenAI  
- Azure OpenAI  
- XAI  
- Open-Source Models  
- Baidu Qianfan  
- Tongyi Qianwen  
- Zhipu AI  

---

## Supported Frameworks

- Flask (>=3.0.0)  
- Django (3, 4, 5)  

---

## Example: API Documentation Web Page

![image](assets/example1.png)

---

## TODO

- Add support for additional models and frameworks.  
