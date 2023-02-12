"""一些功能吧"""
from .general import *
from .image import *
from .database import *
from .update import *
from .help import HELP_DATAS

from nonebot import on_command
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import MessageSegment
import httpx
from nonebot_plugin_imageutils import text2image
from io import BytesIO


update_game_resource = on_command("更新方舟素材")
init_db = on_command("更新方舟数据库")
help_msg = on_command("方舟帮助", aliases={"arkhelp"})


@update_game_resource.handle()
async def _():
    await update_game_resource.send("开始更新游戏素材……")
    async with httpx.AsyncClient() as client:
        await ArknightsGameData(client).download_files()
        await ArknightsDB.init_data()
        await ArknightsGameImage(client).download_files()
    await update_game_resource.finish("游戏数据更新完成！")


@init_db.handle()
async def _():
    await update_game_resource.send("开始更新游戏数据库……")
    await ArknightsDB.init_data()
    await update_game_resource.finish("游戏数据库更新完成！")


@help_msg.handle()
async def _():
    result = "\n".join(
        f"[color=red]{data.name}[/color]"
        f"\n{data.description}"
        f"\n{data.usage}\n"
        for data in HELP_DATAS + [__plugin_meta__]
    )
    output = BytesIO()
    text2image(result).save(output, "png")
    await help_msg.finish(MessageSegment.image(output))


__plugin_meta__ = PluginMetadata(
    name="更新游戏数据",
    description="更新游戏素材、更新本地数据库",
    usage=(
        "命令:"
        "\n    更新方舟素材 => 从Github下载游戏素材(json数据与图片)"
        "\n    更新方舟数据库 => 更新本地sqlite数据库"
    ),
    extra={
        "name": "update_plugin_data",
        "author": "NumberSir<number_sir@126.com>",
        "version": "0.1.0"
    }
)
