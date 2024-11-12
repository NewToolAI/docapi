![image](assets/logo.png)


![Python Version](https://img.shields.io/badge/python-3.8+-aff.svg)
![Lisence](https://img.shields.io/badge/license-Apache%202-dfd.svg)
[![PyPI](https://img.shields.io/pypi/v/docapi)](https://pypi.org/project/docapi/)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/Shulin-Zhang/docapi/pulls)


## docapi是一个用大模型自动生成API文档的python包，会自动扫描API的路由结构，生成或更新API文档。

## 安装

```bash
pip install docapi

或

pip install docapi -i https://pypi.org/simple
```

## 使用方法

### 注意

**使用docapi时必须在api项目的环境中。**

### 方法一
```bash
export OPENAI_API_KEY=your_key

docapi generate server.py

docapi update server.py
```

### 方法二

生成配置文件
```bash
docapi init
```

编辑`config.yaml`文件
```yaml
openai_api_key: xxx

openai_base_url: 'http://ip:port:v1'

openai_model: 'qwen-plus'
```
```bash
docapi generate server.py ./docs --lang zh --config config.yaml

docapi update server.py./docs --lang zh --config config.yaml
```

## 支持模型

- OpenAI

- AzureOpenAI

- 通义千问

## 支持API框架

- Flask

## TODO

- 支持文心一言、智谱AI等大模型

- 支持fastapi、django等框架

- 支持文档在线web页面展示

- 支持自定义文档模版

- 多线程加速请求
