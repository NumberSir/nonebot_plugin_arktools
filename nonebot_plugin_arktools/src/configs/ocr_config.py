from pydantic import BaseModel, Extra


class BaiduOCRConfig(BaseModel, extra=Extra.ignore):
    """公招识别相关配置"""
    arknights_baidu_app_id: str = "vCCBz17TttuhwuyeeOsya3v2"  # 百度 OCR APP ID
    arknights_baidu_api_key: str = "l7U66VjEAKdvoKTROX2xeVM5xGVrfuh6"  # 百度 OCR API KEY


__all__ = [
    "BaiduOCRConfig"
]
