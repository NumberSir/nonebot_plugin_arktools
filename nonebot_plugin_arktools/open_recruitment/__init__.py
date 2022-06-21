from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message
from nonebot.log import logger
from nonebot.params import CommandArg

from .data_source import get_recommend_tags

recruit = on_command("公开招募", aliases={"公招", "方舟公招", "公招tag"}, priority=5, block=True)


@recruit.handle()
async def _(arg: Message = CommandArg()):
    logger.info(f"{arg}")
    taglist = arg.extract_plain_text().strip().split()
    rst = await get_recommend_tags(taglist)

    if rst is None:
        rst = "获取公招推荐数据失败！请检查网络连接并稍后重试"

    if not rst:
        rst = "当前没有必出稀有干员的公招标签"

    await recruit.finish(rst, at_sender=True)