import os
from .config import Config
from nonebot import get_driver
from nonebot import logger
from dataclasses import dataclass

import json
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models
from pathlib import Path
from PIL import Image, ImageFont
from PIL.ImageDraw import Draw, ImageDraw

recruit_config = Config.parse_obj(get_driver().config.dict())
SAVE_PATH = Path(recruit_config.recruitment_save_path)
FONT_PATH = Path(__file__).parent.parent / "_data" / "operator_info" / "font"


def ocr(image_url: str) -> set:
    """调用腾讯云进行 OCR 识别公招标签"""
    with open(Path().parent.parent / "_data" / "operator_info" / "json" / "gacha_table.json", "r", encoding="utf-8") as f:
        TAGS = json.load(f)
    TAGS = {_["tagName"] for _ in TAGS["gachaTags"]}
    try:
        cred = credential.Credential(recruit_config.tencent_cloud_secret_id, recruit_config.tencent_cloud_secret_key)
        client = ocr_client.OcrClient(cred, "ap-beijing")
        req = models.GeneralAccurateOCRRequest()
        params = {"ImageUrl": image_url}
        req.from_json_string(json.dumps(params))
        resp = client.GeneralAccurateOCR(req)
        data = json.loads(resp.to_json_string())

    except TencentCloudSDKException as e:
        logger.error(f"腾讯云识别公招标签出错: {e}")
        return set()

    else:
        filtered_char: set = {f"{i}" for i in range(10)}.union({chr(i) for i in range(65, 90)})  # 过滤字母和数字
        pre_tags = {word["DetectedText"] for word in data["TextDetections"] if all(c not in word["DetectedText"] for c in filtered_char)}

        return {tag for tag in pre_tags if tag in TAGS}


@dataclass
class Operator:
    code: str
    name: str
    prof: str
    pos: str
    tags: list
    rarity: int
    sex: bool = 0


def load_operator_data() -> dict:
    """读取干员基本信息：职业、位置、性别、标签、稀有度"""
    operators = {}
    with open(Path().parent / "json" / "character_table.json", "r", encoding="utf-8") as f:
        operator_basic_info: dict = json.load(f)

    with open(Path().parent / "json" / "handbook_info_table.json", "r", encoding="utf-8") as f:
        operator_data_info: dict = json.load(f)

    with open(Path().parent / "json" / "gacha_table.json", "r", encoding="utf-8") as f:
        operator_obtainable: dict = json.load(f)

    for code, info in operator_basic_info.items():
        if not info["itemObtainApproach"]:
            continue
        if info["itemObtainApproach"] != "招募寻访":
            continue
        if info["isSpChar"]:
            continue
        if info["name"] not in operator_obtainable["recruitDetail"]:
            continue
        operator = Operator(
            code=code,
            name=info["name"],
            prof=info["profession"],
            rarity=info["rarity"],
            tags=info["tagList"],
            pos=info["position"]
        )
        operators[code] = operator

    for code, info in operator_data_info["handbookDict"].items():
        if code not in operators:
            continue

        if "男" in info["storyTextAudio"][0]["stories"][0]["storyText"]:
            operators[code].sex = 1

    return operators


def get_rare_operators(tags: set) -> list:
    """
    获取干员
    性别 -> 男/女
    职业 -> 先锋/近卫/重装/狙击/术师/医疗/辅助/特种
    位置 -> 近战/远程
    高资 -> 六星
    资深 -> 五星
    """
    profession = {}
    position = {}
    sex = {}
    rarity = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    general = {}

    with open(Path().parent / "json" / "recruitment_tags.json", "r", encoding="utf-8") as f:
        tags_cate = json.load(f)

    operators = load_operator_data()

    for tag in tags:
        if tag in tags_cate["资质"]:
            if tag == "新手":
                rarity[1] = "1"
            elif tag == "资深干员":
                rarity[4] = tag
            elif tag == "高级资深干员":
                rarity[5] = tag
            else:
                rarity[0] = tag
        elif tag in tags_cate["性别"]:
            if tag == "男性干员":
                sex[1] = tag
            else:
                sex[0] = tag
        elif tag in tags_cate["位置"]:
            if tag == "近战位":
                position["MELEE"] = tag
            else:
                position["RANGED"] = tag
        elif tag in tags_cate["职业"]:
            if tag == "先锋干员":
                profession["PIONEER"] = tag
            elif tag == "医疗干员":
                profession["MEDIC"] = tag
            elif tag == "术师干员":
                profession["CASTER"] = tag
            elif tag == "特种干员":
                profession["SPECIAL"] = tag
            elif tag == "狙击干员":
                profession["SNIPER"] = tag
            elif tag == "辅助干员":
                profession["SUPPORT"] = tag
            elif tag == "近卫干员":
                profession["WARRIOR"] = tag
            elif tag == "重装干员":
                profession["TANK"] = tag
        else:
            general[tag] = tag

    result = {}
    for code, op in operators.items():
        if op.rarity in rarity:
            if op.code in result:
                continue
            result[op.code] = {"code": op.code, "name": op.name, "rarity": op.rarity, "tags": [str(rarity[op.rarity])]}

            if op.prof in profession:
                result[op.code]["tags"].append(profession[op.prof])
            if op.pos in position:
                result[op.code]["tags"].append(position[op.pos])
            if op.sex in sex:
                result[op.code]["tags"].append(sex[op.sex])

        for t in op.tags:
            if t in general and op.rarity in rarity:
                result[op.code]["tags"].append(general[t])

    # pprint(result)
    result_list = []
    for _, __ in result.copy().items():
        tags = sorted([t for t in __["tags"] if t not in {"0", "1", "2", "3", "4"}])
        if not tags:  # 剔除占位用
            continue

        mapping = [
            (data["name"], data["code"], data["rarity"])
            for code, data in result.copy().items()
            if sorted([
                t
                for t in data["tags"]
                if t not in {"0", "1", "2", "3", "4"}
            ]) == tags
        ]

        if {"tags": tags, "operators": mapping} in result_list:
            continue

        if not any(any(i in m for i in {1, 2}) for m in mapping):
            result_list.append({"tags": tags, "operators": mapping})

    return result_list


def text_border(text: str, draw: ImageDraw, x: int, y: int, font: ImageFont, shadow_colour: tuple, fill_colour: tuple, anchor: str = "la"):
    """文字加边框"""
    draw.text((x - 1, y), text=text, anchor=anchor, font=font, fill=shadow_colour)
    draw.text((x + 1, y), text=text, anchor=anchor, font=font, fill=shadow_colour)
    draw.text((x, y - 1), text=text, anchor=anchor, font=font, fill=shadow_colour)
    draw.text((x, y + 1), text=text, anchor=anchor, font=font, fill=shadow_colour)

    draw.text((x - 1, y - 1), text=text, anchor=anchor, font=font, fill=shadow_colour)
    draw.text((x + 1, y - 1), text=text, anchor=anchor, font=font, fill=shadow_colour)
    draw.text((x - 1, y + 1), text=text, anchor=anchor, font=font, fill=shadow_colour)
    draw.text((x + 1, y + 1), text=text, anchor=anchor, font=font, fill=shadow_colour)

    draw.text((x, y), text=text, anchor=anchor, font=font, fill=fill_colour)


def build_image(result_list: list) -> Image:
    font = ImageFont.truetype(str(FONT_PATH / "Arknights-zh.otf"), 24)
    if not result_list:
        return None

    main_background = Image.new(mode="RGBA", size=(2002, 3360), color=(50, 50, 50, 255))
    pri_height = 0
    pri_width = 0
    H = 0

    for data in result_list:
        L = len(data["operators"])
        tag_background = Image.new(mode="RGBA", size=(956, 168 * (L // 6 + 1)), color=(100, 100, 100, 0))  # TAG + 6干员图
        tags = data["tags"]
        L = len(tags)
        tag_bg = Image.new(mode="RGBA", size=(144, 168), color=(0, 0, 0, 0))
        for tag_idx, tag in enumerate(tags):
            text_border(text=tag, draw=Draw(tag_bg), x=72, y=102 - 18 * L + 36 * tag_idx, anchor="mm", font=font, shadow_colour=(0, 0, 0, 255), fill_colour=(255, 255, 255, 255))
        tag_background.paste(tag_bg, box=(0, 0), mask=tag_bg.split()[3])

        for op_idx, op in enumerate(data["operators"]):
            op_background = Image.new(mode="RGBA", size=(128, 164), color=(0, 0, 0, 0))  # 干员头图+名称
            avatar = Image.open(Path().parent / "avatar" / f"{op[1]}.png").convert("RGBA").resize((128, 128))  # 头像
            name = op[0]
            op_background.paste(im=avatar, mask=avatar.split()[3])
            text_border(text=op[0], draw=Draw(op_background), x=64, y=150, anchor="mm", font=font, shadow_colour=(0, 0, 0, 255), fill_colour=(255, 255, 255, 255))
            tag_background.paste(im=op_background, box=(168 + 132 * (op_idx % 6), 2 + 168 * (op_idx // 6)))

        if pri_height == 0:
            if pri_width != 0:
                main_background.paste(im=tag_background, mask=tag_background.split()[3], box=(pri_width + 24, 24))
            else:
                main_background.paste(im=tag_background, mask=tag_background.split()[3], box=(24, 24))
        elif pri_width != 0:
            main_background.paste(im=tag_background, mask=tag_background.split()[3], box=(pri_width + 24, pri_height + 42))
        else:
            main_background.paste(im=tag_background, mask=tag_background.split()[3], box=(24, pri_height + 42))
        pri_height += 24 + tag_background.size[1]
        if pri_height > 1200:
            H = pri_height
            pri_width = 998
            pri_height = 0

        draw = Draw(main_background)
        if pri_width == 0:
            draw.line(xy=(0, pri_height + 21, 1001 - 2, pri_height + 21))
        elif pri_height != 0:
            draw.line(xy=(1001 - 2, pri_height + 21, 2002, pri_height + 21))

    h = max(H, pri_height) + 24

    if pri_width != 0:
        main_background = main_background.crop((0, 0, 2002, h))
    else:
        main_background = main_background.crop((0, 0, 1004, h))
    draw = Draw(main_background)
    draw.line(xy=(0, 0, main_background.size[0], 0), fill=(190, 190, 190, 255), width=4)
    draw.line(xy=(0, 0, 0, h), fill=(190, 190, 190, 255), width=4)
    draw.line(xy=(main_background.size[0] - 2, 0, main_background.size[0] - 2, h), fill=(190, 190, 190, 255), width=4)
    draw.line(xy=(0, h - 2, main_background.size[0] - 2, h - 2), fill=(190, 190, 190, 255), width=4)

    draw.line(xy=(1001 - 2, 0, 1001 - 2, h - 2), fill=(190, 190, 190, 255), width=2)
    file = SAVE_PATH / "temp.png"
    None if os.path.exists(SAVE_PATH) else os.mkdir(SAVE_PATH)
    main_background.save(file)
    return file

    
