# ![image](assets/logo.png)

![Python Version](https://img.shields.io/badge/python-3.8+-aff.svg)
![OS](https://img.shields.io/badge/os-windows%20|%20linux%20|%20macos-blue)
![License](https://img.shields.io/badge/license-Apache%202-dfd.svg)
[![PyPI](https://img.shields.io/pypi/v/docapi)](https://pypi.org/project/docapi/)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/Shulin-Zhang/docapi/pulls)

\[ [中文](README_zh.md) | English \]

**DocAPI** is an API documentation generation tool based on large language models (LLM), currently supporting Flask and Django frameworks. With DocAPI, you can quickly generate, update, and display API documentation, significantly enhancing development efficiency.

---

## Important Notes

- **Version 1.x.x** introduces significant changes compared to **0.x.x**. Please refer to the latest usage guide below.
- By default, generating or updating documentation requires the API service's dependency environment.
- Use the parameter `--static` for static route scanning that does not depend on the project environment, only supported for Flask projects. The downside is that it may include unused routes in the documentation, suitable for single-page Flask API projects.

---

## Core Features

- **Framework Support**: Automatically scans the route structure of Flask and Django services.
- **Multi-Model Compatibility**: Supports various mainstream commercial and open-source large models.
- **Documentation Operations**: Automatically generates complete documentation and updates parts of the documentation.
- **Multi-Language Support**: Generates multi-language API documentation (requires LLM support).
- **Web Display**: Supports displaying API documentation through a web page.

---

## Changelog

- [2025-01-24]: Support for Deepseek, Moonshot, Baichuan, Doubao models.
- [2024-12-16]: Displays progress bar when generating or updating documentation; Flask projects support static route scanning without project environment dependency.
- [2024-12-05]: Full support for Django versions 3, 4, and 5 with completed testing.
- [2024-12-02]: Windows system testing passed (requires PowerShell or Windows Terminal), optimized model name management to avoid environment variable conflicts.
- [2024-11-26]: Supports loading environment variables from `.env` files and multi-language documentation.
- [2024-11-24]: Introduced multithreading to accelerate request processing.
- [2024-11-20]: Added support for custom documentation templates.
- [2024-11-17]: Support for Zhipu AI and Baidu Qianfan models, optimized documentation structure, added JavaScript example code; removed configuration file execution mode.

---

## Installation

Install the latest version via PyPI:

```bash
pip install -U docapi
```

Install the version with all dependencies:

```bash
pip install -U "docapi[all]"
```

Install with support for a specific framework only:

```bash
pip install -U "docapi[flask]"
```

```bash
pip install -U "docapi[django]"
```

Install from the official PyPI source:

```bash
pip install -U "docapi[all]" -i https://pypi.org/simple
```

Install from GitHub:

```bash
pip install git+https://github.com/Shulin-Zhang/docapi
 ```

## Usage Guide
Below are typical usage examples:

### OpenAI Model Example 1. Configure Model and Key:
```bash
export DOCAPI_MODEL=openai:gpt-4o-mini

export OPENAI_API_KEY=your_api_key
 ```
 2. Generate Documentation:
- Flask Service:
```bash
docapi generate server.py

# Static route scanning, does not depend on the project environment
# docapi generate server.py --static
```

- Django Service:
```bash
docapi generate manage.py
 ```
 3. Update Documentation:
- Flask Service:
```bash
docapi update server.py

# Static route scanning, does not depend on the project environment
# docapi update server.py --static
 ```

- Django Service:
```bash
docapi update manage.py
 ```
 4. Start Web Service to Display Documentation:
```bash
docapi serve
 ```

### [For more usage, please refer to](USAGE.md)

---

## Supported Models
- OpenAI
- Azure OpenAI
- XAI
- Open Source Models
- Baidu Qianfan
- Tongyi Qianwen
- Zhipu AI
- Deepseek
- (Kimi) Moonshot
- Doubao
- Baichuan

## Supported Frameworks
- Flask (>=3.0.0)
- Django (3, 4, 5)

## Example: API Documentation Web Page
![image](assets/example1.png)

## TODO
- Support more large models and API frameworks.
