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

- **Version 1.x.x** introduces significant changes compared to **Version 0.x.x**. Please refer to the updated usage guide below.  
- By default, generating or updating documentation requires the API service's dependency environment.  
- Add the `--static` parameter for static route scanning that does not depend on the project environment. This option only supports Flask projects. The downside is that it may include unused routes in the generated documentation. It suitable for single-page Flask API projects.  

---

## Key Features

- **Framework Support**: Automatically scans routing structures for Flask and Django applications.  
- **Multi-Model Compatibility**: Works with a wide range of commercial and open-source LLMs.  
- **Documentation Management**: Generates complete documentation or performs incremental updates.  
- **Multi-Language Support**: Creates multilingual API documentation (requires LLM support).  
- **Web Integration**: Supports deploying documentation on a web interface.

---

## Changelog

- [2024-12-16]: Display a progress bar when generating or updating documentation; The Flask project supports static route scanning independent of the project environment.
- [2024-12-05]: Fully supported Django versions 3, 4, and 5, with comprehensive testing completed.  
- [2024-12-02]: Passed Windows system testing (requires PowerShell or Windows Terminal). Optimized model name management to avoid conflicts with environment variables.  
- [2024-11-26]: Added support for loading environment variables from `.env` files and multilingual documentation.  
- [2024-11-24]: Introduced multithreading to accelerate request processing.  
- [2024-11-20]: Added support for custom documentation templates.  
- [2024-11-17]: Supported Zhipu AI and Baidu Qianfan models, improved documentation structure, and added JavaScript example code. Removed configuration file execution mode.  
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

# Static route scanning, independent of the project environment.
# docapi generate server.py --static
```
- For Django:
```bash
docapi generate manage.py
```

#### 3. Update documentation:
- For Flask:
```bash
docapi update server.py

# Static route scanning, independent of the project environment.
# docapi update server.py --static
```

- For Django:
```bash
docapi update manage.py
```

#### 4. Start a web server to display the documentation:
```bash
docapi serve
```

[Find more usage details in the guide](USAGE.md).

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
