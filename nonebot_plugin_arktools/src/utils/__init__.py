"""一些功能吧"""
from .general import *
from .image import *
from .database import *
from .update import *

from nonebot import on_command, logger
from nonebot.plugin import PluginMetadata
import httpx


update_game_resource = on_command("更新方舟素材")
init_db = on_command("更新方舟数据库")


@update_game_resource.handle()
async def _():
    await update_game_resource.send("开始更新游戏素材……")
    try:
        async with httpx.AsyncClient() as client:
            await ArknightsGameData(client).download_files()
            await ArknightsDB.init_data()
            await ArknightsGameImage(client).download_files()
    except httpx.ConnectError as e:
        logger.warning("下载方舟额外素材出错，请修改代理或重试")
        await update_game_resource.finish("下载方舟额外素材出错，请修改代理或重试")
    else:
        await update_game_resource.finish("游戏数据更新完成！")


@init_db.handle()
async def _():
    await update_game_resource.send("开始更新游戏数据库……")
    await ArknightsDB.init_data()
    await update_game_resource.finish("游戏数据库更新完成！")


__plugin_meta__ = PluginMetadata(
    name="杂项",
    description="查看指令列表、更新游戏素材、更新本地数据库",
    usage=(
        "命令:"
        "\n    方舟帮助 => 查看指令列表"
        "\n    更新方舟素材 => 从Github下载游戏素材(json数据与图片)"
        "\n    更新方舟数据库 => 更新本地sqlite数据库"
    ),
    extra={
        "name": "update_plugin_data",
        "author": "NumberSir<number_sir@126.com>",
        "version": "0.1.0"
    }
)
