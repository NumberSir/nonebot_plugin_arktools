from pydantic import BaseModel, Extra


class BaiduOCRConfig(BaseModel, extra=Extra.ignore):
    """公招识别相关配置"""
    arknights_baidu_app_id: str
    arknights_baidu_api_key: str


__all__ = [
    "BaiduOCRConfig"
]
