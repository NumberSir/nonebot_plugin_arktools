from pydantic import BaseModel, Extra


class ProxyConfig(BaseModel, extra=Extra.ignore):
    """github代理相关配置"""
    github_raw: str = "https://raw.githubusercontent.com"  # 资源网址
    github_site: str = "https://github.com"  # 访问网址


__all__ = [
    "ProxyConfig"
]
