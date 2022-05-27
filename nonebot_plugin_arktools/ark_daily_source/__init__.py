"""每日开放资源关卡"""
import nonebot
from nonebot import logger
from nonebot import on_regex
from nonebot_plugin_apscheduler import scheduler

from .config import Config
from .data_source import get_daily_sources

global_config = nonebot.get_driver().config
ark_daily_config = Config(**global_config.dict())

__zx_plugin_name__ = "今日方舟资源"
__plugin_usage__ = """
usage：
    看看方舟今天哪些资源关开放
    指令：
        今日方舟 / 今日方舟资源
""".strip()
__plugin_superuser_usage__ = """
usage：
    更新今日方舟资源
    指令：
        更新今日方舟资源
""".strip()
__plugin_des__ = "看看方舟今天哪些资源关开放"
__plugin_cmd__ = ["今日方舟/今日方舟资源", "更新今日方舟资源 [_superuser]"]
__plugin_type__ = ("方舟相关",)
__plugin_version__ = 0.1
__plugin_author__ = "Number_Sir"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["今日方舟", "今日方舟资源"],
}

material = on_regex(r"[今日|天]*方舟[今日|天]*[资源]*[材料]*", priority=5, block=True)
super_cmd = on_regex(r"更新[今日|天]*方舟[今日|天]*[资源]*[材料]*", permission=SUPERUSER, priority=1, block=True)


@material.handle()
async def _():
    rst_img = await get_daily_sources()
    if rst_img:
        rst = rst_img
    else:
        rst = f"方舟每日资源截图失败！请更换至非windows平台部署本插件\n或检查网络连接并稍后重试"
    await material.finish(rst)


@super_cmd.handle()
async def _():
    try:
        await get_daily_sources(is_force=True)
    except Exception as e:
        logger.error(f"每日方舟资源更新失败！{type(e)}: {e}")
        await super_cmd.finish(f"每日方舟资源更新失败！请稍后重试！")
    else:
        await super_cmd.finish(f"每日方舟资源更新完成！")


@scheduler.scheduled_job(
    "cron",
    hour=4,
    minute=1,
)
async def _():
    try:
        await get_daily_sources(is_force=True)
    except Exception as e:
        logger.error(f"每日方舟资源更新失败！{type(e)}: {e}")
