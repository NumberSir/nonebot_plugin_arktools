import nonebot
from .ark_daily_source import *
from .activity_notice import *
from ._utils import *

driver = nonebot.get_driver()
@driver.on_startup
async def _():
    nonebot.load_plugins("./nonebot_plugin_arktools")
