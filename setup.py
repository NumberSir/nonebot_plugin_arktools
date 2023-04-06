import setuptools


with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="nonebot_plugin_arktools",
    version="1.0.18",
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
        'nonebot-adapter-onebot>=2.2.0',
        'nonebot2>=2.0.0rc2',
        'nonebot-plugin-apscheduler>=0.2.0',
        'nonebot-plugin-imageutils>=0.1.14',
        'nonebot-plugin-htmlrender>=0.2.0.1',

        'httpx>=0.23.1',
        'aiofiles>=0.8.0',
        'tortoise-orm>=0.19.3',
        'lxml>=4.9.2',
        'feedparser>=6.0.10',
    ],
    python_requires=">=3.8"
)
