"""获取干员信息"""
from nonebot import on_command
from nonebot.exception import ActionFailed
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Message, MessageSegment

from .data_source import *

query_operator = on_command("干员", aliases={"方舟干员", "明日方舟干员"})


@query_operator.handle()
async def _(arg: Message = CommandArg()):
    try:
        name = arg.extract_plain_text().strip()
        op = OperatorInfo(name)
        build = BuildOperatorImage(op)
        img = build.build_whole_image()

        img = MessageSegment.image(img)
        await query_operator.finish(Message(img))
    except ActionFailed as e:
        await query_operator.finish("图片发送失败！", at_sender=True)