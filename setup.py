from setuptools import setup, find_packages

# 读取 README.md 内容作为项目长描述
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="docapi",  # 包名
    version="0.1.1",  # 初始版本号
    author="ZhangShulin",
    author_email="zhangslwork@yeah.net",
    description="DocAPI is a Python package that automatically generates API documentation using LLM.",
    keywords="llmdoc, autodoc, apidoc, docapi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shulin-Zhang/docapi",  # 项目主页
    packages=find_packages(),  # 自动查找项目中的所有包
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",  # 许可证类型（可根据需要更改）
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  # 最低 Python 版本要求
    entry_points={
        "console_scripts": [
            "docapi=docapi.main:run",
        ],
    },
)

