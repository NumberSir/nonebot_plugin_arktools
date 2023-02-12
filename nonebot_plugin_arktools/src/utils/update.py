import asyncio
from pathlib import Path
from typing import List, Dict
from aiofiles import open as aopen, os as aos
from lxml import etree
from urllib.parse import quote, unquote
from nonebot import logger, get_driver

import httpx

from ..configs.path_config import PathConfig

driver = get_driver()
pcfg = PathConfig.parse_obj(get_driver().config.dict())

BASE_URL = "https://raw.kgithub.com"  # 镜像

REPOSITORIES = {
    "gamedata": "/Kengxxiao/ArknightsGameData/master",
    "gameimage_1": "/yuanyan3060/Arknights-Bot-Resource/master",
    "gameimage_2": "/Aceship/Arknight-Images/master",
}

FILES = {
    "gamedata": [
        "zh_CN/gamedata/excel/building_data.json",          # 基建技能，制造配方
        "zh_CN/gamedata/excel/char_patch_table.json",       # 升变阿米娅
        "zh_CN/gamedata/excel/character_table.json",        # 干员表
        "zh_CN/gamedata/excel/data_version.txt",            # 数据版本
        "zh_CN/gamedata/excel/gamedata_const.json",         # 游戏常数
        "zh_CN/gamedata/excel/gacha_table.json",            # 公招相关
        "zh_CN/gamedata/excel/item_table.json",   # 物品表
        "zh_CN/gamedata/excel/handbook_info_table.json",    # 档案表
        "zh_CN/gamedata/excel/skill_table.json",  # 技能表
        "zh_CN/gamedata/excel/uniequip_table.json",         # 模组表、子职业映射
        "zh_CN/gamedata/excel/handbook_team_table.json",    # 干员阵营
    ]
}

DIRS = {
    "gamedata": [
        "/zh_CN/gamedata/excel"
    ],
    "gameimage_1": [
        "item"
    ],
    "gameimage_2": [
        "avatars",  # 头像 (180x180)
        "characters",  # 立绘 (1024x1024 | 2048x2048)
        "classes",  # 职业图标 (255x255)
        "equip/icon",  # 模组图标 (511x511)
        "equip/stage",  # 模组阶段图标 (174x160)
        "equip/type",  # 模组分类图标
        "factions",  # 阵营 (510x510)
        # "items",  # 物品图标
        # "material",  # 材料图标
        # "material/bg",  # 材料背景图标 (190x190)
        "portraits",  # 画像 (180x360)
        "skills",  # 技能图标 (128x128)
        "ui/chara",  # 公招出货表层贴图
        "ui/elite",  # 精英化图标
        "ui/infrastructure",  # 基建技能分类图标
        "ui/infrastructure/skill",  # 基建技能图标
        "ui/potential",  # 潜能图标
        "ui/rank",  # 专精图标、技能升级图标
        "ui/subclass",  # 子职业图标
    ]
}


class ArknightsGameData:
    def __init__(self, client: httpx.AsyncClient = None):
        self._url = f"{BASE_URL}{REPOSITORIES['gamedata']}"
        self._client = client or httpx.AsyncClient()

    async def get_local_version(self) -> str:
        """获取本地版本"""
        try:
            async with aopen(pcfg.arknights_gamedata_path / "excel" / "data_version.txt") as fp:
                data = await fp.read()
        except FileNotFoundError as e:
            return ""
        return data.split("\n")[-2].split(":")[1]

    async def get_latest_version(self) -> str:
        """获取最新版本"""
        url = f"{self._url}/zh_CN/gamedata/excel/data_version.txt"
        response = await self._client.get(url)
        return response.text.split("\n")[-2].split(":")[1]  # eg: "31.4.0"

    async def is_update_needed(self) -> bool:
        """是否要更新"""
        return await self.get_local_version() != await self.get_latest_version()

    async def download_files(self):
        """下载gamedata"""
        tmp = Path(__file__).absolute().parent.parent.parent / "data" / "arknights" / "gamedata" / "excel"
        await aos.makedirs(tmp, exist_ok=True)
        logger.info("##### ARKNIGHTS GAMEDATA DOWNLOAD BEGIN ")

        tasks = [
            self.save(self._url, file, tmp)
            for file in FILES['gamedata']
        ]
        await asyncio.gather(*tasks)
        logger.info("===== ARKNIGHTS GAMEDATA DOWNLOAD DONE ")

    async def save(self, url: str, file: str, tmp: Path):
        """异步gather用"""
        content = (await self._client.get(f"{url}/{file}", timeout=100)).content
        async with aopen(tmp / file.split('/')[-1], "wb") as fp:
            await fp.write(content)
        logger.info(f"\t- Arknights-Data downloaded: {file.split('/')[-1]}")


class ArknightsGameImage:
    def __init__(self, client: httpx.AsyncClient = None):
        self._client = client or httpx.AsyncClient()
        self._urls: List[str] = []
        self._htmls: Dict[str, str] = {}

    async def download_files(self):
        """下载gameimage"""
        tmp = Path(__file__).absolute().parent.parent.parent / "data" / "arknights" / "gameimage"
        await aos.makedirs(tmp, exist_ok=True)
        logger.info("##### ARKNIGHTS GAMEIMAGE DOWNLOAD BEGIN ")

        logger.info("\t### REQUESTING FILE LISTS ... ")
        tasks = []
        for dir_ in DIRS['gameimage_1']:
            await aos.makedirs(tmp / dir_, exist_ok=True)
            url = f"https://kgithub.com/yuanyan3060/Arknights-Bot-Resource/file-list/main/{dir_}"
            tasks.append(self.get_htmls(url, dir_))
            # logger.info(f"\t\t# REQUESTING {url} ... ")
        for dir_ in DIRS['gameimage_2']:
            await aos.makedirs(tmp / dir_, exist_ok=True)
            url = f"https://kgithub.com/Aceship/Arknight-Images/file-list/main/{dir_}"
            tasks.append(self.get_htmls(url, dir_))
            # logger.info(f"\t\t# REQUESTING {url} ... ")
        await asyncio.gather(*tasks)

        logger.info("\t### REQUESTING REPOS ... ")
        for dir_, (html, url) in self._htmls.items():
            # logger.info(f"\t\t# REQUESTING {url} ... ")
            dom = etree.HTML(html, etree.HTMLParser())
            file_names: List[str] = dom.xpath(
                "//a[@class='js-navigation-open Link--primary']/text()"
            )
            if REPOSITORIES["gameimage_1"].split("/")[1] in url:
                self._urls.extend(
                    f"{BASE_URL}{REPOSITORIES['gameimage_1']}/{dir_}/{file_name}"
                    for file_name in file_names

                    if "recruitment" not in file_name
                    # and "token_" not in file_name
                    and "ap_" not in file_name
                    and "clue_" not in file_name
                    and "itempack_" not in file_name
                    and "LIMITED_" not in file_name
                    and "LMTGS_" not in file_name
                    and "p_char_" not in file_name
                    and "randomMaterial" not in file_name
                    and "tier" not in file_name
                )
            elif REPOSITORIES["gameimage_2"].split("/")[1] in url:
                if "avatars" in dir_ or "portraits" in dir_:
                    self._urls.extend(
                        f"{BASE_URL}{REPOSITORIES['gameimage_2']}/{dir_}/{file_name}"
                        for file_name in file_names

                        if "#" not in file_name  # 不要皮肤，太大了
                        and "char" in file_name
                        and "+.png" not in file_name
                    )
                elif "characters" in dir_:
                    self._urls.extend(
                        f"{BASE_URL}{REPOSITORIES['gameimage_2']}/{dir_}/{file_name}"
                        for file_name in file_names

                        if "#" not in file_name  # 不要皮肤，太大了
                        and "b.png" not in file_name
                    )
                else:
                    self._urls.extend(
                        f"{BASE_URL}{REPOSITORIES['gameimage_2']}/{dir_}/{file_name}"
                        for file_name in file_names
                    )

        tasks = [self.save(url, tmp) for url in self._urls if not (tmp / url.split('/master/')[-1]).exists()]
        await asyncio.gather(*tasks)
        logger.info("===== ARKNIGHTS GAMEIMAGE DOWNLOAD DONE ")

    async def get_htmls(self, url: str, dir_: str):
        """异步gather用"""
        html = (await self._client.get(url, timeout=100)).text
        self._htmls[dir_] = (html, url)

    async def save(self, url: str, tmp: Path):
        """异步gather用"""
        # print(url)
        content = (await self._client.get(quote(url, safe="/:"), timeout=100)).content
        if not url.endswith(".png"):
            return
        async with aopen(tmp / unquote(url).split('/master/')[-1], "wb") as fp:
            await fp.write(content)
        logger.info(f"\t- Arknights-Image downloaded: {unquote(url).split('/master/')[-1]}")


async def download_extra_files(client: httpx.AsyncClient):
    """下载字体、猜干员的图片素材"""
    urls = [
        f"{BASE_URL}/NumberSir/nonebot_plugin_arktools/main/nonebot_plugin_arktools/data/fonts/Arknights-en.ttf",
        f"{BASE_URL}/NumberSir/nonebot_plugin_arktools/main/nonebot_plugin_arktools/data/fonts/Arknights-zh.otf",
        f"{BASE_URL}/NumberSir/nonebot_plugin_arktools/main/nonebot_plugin_arktools/data/guess_character/correct.png",
        f"{BASE_URL}/NumberSir/nonebot_plugin_arktools/main/nonebot_plugin_arktools/data/guess_character/down.png",
        f"{BASE_URL}/NumberSir/nonebot_plugin_arktools/main/nonebot_plugin_arktools/data/guess_character/up.png",
        f"{BASE_URL}/NumberSir/nonebot_plugin_arktools/main/nonebot_plugin_arktools/data/guess_character/vague.png",
        f"{BASE_URL}/NumberSir/nonebot_plugin_arktools/main/nonebot_plugin_arktools/data/guess_character/wrong.png",
    ]
    logger.info("##### EXTRA FILES DOWNLOAD BEGIN")
    for url in urls:
        path = url.split("data/")[-1]
        if (pcfg.arknights_data_path / path).exists():
            continue
        response = await client.get(url)
        async with aopen(pcfg.arknights_data_path / path, "wb") as fp:
            await fp.write(response.content)
            logger.info(f"\t- Extra file downloaded: {path}")
    logger.info("===== EXTRA FILES DOWNLOAD DONE")


@driver.on_startup
async def _init_game_files():
    async with httpx.AsyncClient() as client:
        await download_extra_files(client)
        logger.info("检查方舟游戏素材版本中 ...")
        if not await ArknightsGameData(client).is_update_needed():
            logger.info("方舟游戏素材当前为最新！")
            return
        await ArknightsGameData(client).download_files()
        await ArknightsGameImage(client).download_files()


__all__ = [
    "ArknightsGameImage",
    "ArknightsGameData"
]