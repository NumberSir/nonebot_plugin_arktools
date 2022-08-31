from nonebot import on_command, logger
from nonebot.internal.params import Arg
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message, GroupMessageEvent, MessageSegment
from .data_source import ocr, get_rare_operators, build_image
from nonebot.exception import ActionFailed

recruit = on_command("公招", aliases={"方舟公招", "公开招募"}, priority=5, block=True)


@recruit.handle()
async def _(matcher: Matcher, event: GroupMessageEvent):
    if event.reply:
        event.message = event.reply.message

    if event.message.get("image", None):  # 自带图片
        for img in event.message["image"]:
            img_url = img.data.get("url", "")
            matcher.set_arg("image", img_url)


@recruit.got(key="image", prompt="请发送公招截图:")
async def _(image: Message = Arg()):
    logger.info(f"image: {image}")
    if isinstance(image, str):
        img_url = image
    else:
        img_url = image["image"][0].data.get("url", "")
    await recruit.send("识别中...")
    tags = ocr(image_url=img_url)
    recruit_list = get_rare_operators(tags)
    if not recruit_list:
        await recruit.finish("没有必出稀有干员的标签组合哦！", at_sender=True)
    image = build_image(recruit_list)
    img = MessageSegment.image(image)
    try:
        await recruit.finish(Message(img))
    except ActionFailed as e:
        await recruit.finish(f"图片发送失败：{e}")
