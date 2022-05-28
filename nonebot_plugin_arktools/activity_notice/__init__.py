"""剿灭、蚀刻章、合约等活动到期提醒"""
import nonebot
from nonebot.log import logger
from nonebot import on_regex
from nonebot_plugin_apscheduler import scheduler
import os

from .config import Config
from .data_source import get_activities


global_config = nonebot.get_driver().config
activity_config = Config(**global_config.dict())

latest_activity = on_regex(r'[查看询]*方舟[最]*新+[活动闻]*', priority=5, block=True)


@latest_activity.handle()
async def _():
    rst_msg = await get_activities(is_force=True)
    if rst_msg:
        await latest_activity.finish(rst_msg)
    else:
        await latest_activity.finish(f"方舟最新活动截图失败！请更换至非windows平台部署本插件\n或检查网络连接并稍后重试", at_sender=True)


@scheduler.scheduled_job(
    "cron",
    hour=4,
    minute=1,
)
async def _():
    try:
        await get_activities(is_force=True, is_cover=True)
    except Exception as e:
        logger.error(f"方舟最新活动检查失败！{type(e)}: {e}")


driver = nonebot.get_driver()
@driver.on_startup
async def _():
    if not os.path.exists(activity_config.activities_data_path):
        os.makedirs(activity_config.activities_data_path)
    if not os.path.exists(activity_config.activities_img_path):
        os.makedirs(activity_config.activities_img_path)
    await get_activities(is_force=True)
