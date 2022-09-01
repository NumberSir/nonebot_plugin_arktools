import setuptools


with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="nonebot_plugin_arktools",
    version="0.5.3",
    author="Number_Sir",
    author_email="Number_Sir@126.com",
    keywords=["pip", "nonebot2", "nonebot", "nonebot_plugin"],
    description="""基于 OneBot 适配器的 NoneBot2 明日方舟小工具箱插件""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NumberSir/nonebot_plugin_arktools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=[
        'nonebot-adapter-onebot>=2.0.0-beta.1',
        'nonebot2>=2.0.0-beta.1',
        'httpx>=0.22.0',
        'pillow>=8.2.0',
        'playwright>=1.22.0',
        'lxml>=4.8.0',
        'tencentcloud-sdk-python>=3.0.675'
    ],
    python_requires=">=3.7.3"
)
