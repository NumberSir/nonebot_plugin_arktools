"""路径设置"""
from pydantic import BaseModel, Extra
from pathlib import Path

SRC_PATH = Path(__file__).absolute().parent.parent


class PathConfig(BaseModel, extra=Extra.ignore):
    """游戏资源 & 数据库路径设置"""
    arknights_data_path: Path = SRC_PATH.parent / "data"
    arknights_font_path: Path = arknights_data_path / "fonts"
    arknights_gamedata_path: Path = arknights_data_path / "arknights" / "gamedata"
    arknights_gameimage_path: Path = arknights_data_path / "arknights" / "gameimage"
    arknights_update_config_path: Path = arknights_data_path / "update"
    arknights_update_cache_path: Path = arknights_data_path / "update" / "cache"

    arknights_configs_path: Path = arknights_data_path / "configs"

    arknights_db_url = arknights_data_path / "databases" / "arknights_sqlite.sqlite3"


__all__ = [
    "PathConfig"
]
