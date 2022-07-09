from .._utils import request_
from typing import List


TAGS = [
    "近卫干员", "狙击干员", "重装干员", "医疗干员", "辅助干员", "术士干员", "特种干员", "先锋干员",
    "近战位", "远程位", "高级资深干员", "资深干员", "支援机械", "男性干员", "女性干员",
    "控场", "爆发", "治疗", "支援", "新手", "费用回复", "输出", "生存", "群攻", "防护", "减速",
    "削弱", "快速复活", "位移", "召唤"
]


async def get_recommend_tags(taglist: List[str]):
    taglist = await preprocess_tags(taglist)

    url = "http://110.40.221.138:8000/api/ark/tools/recruit/recommend"
    headers = {"accept": "application/json"}
    data = {"tags": taglist}
    response = await request_(url=url, headers=headers, data=data, method='POST')

    if response.status_code != 200:
        return None

    recommend_datas = response.json()['recruitRecommends']
    result = ""
    for data in recommend_datas:
        tags_info = data['recommendTags']
        operator_info = data['recommendOperatorInfos']
        operators = {}
        for op in operator_info:
            if op['rarity'] in operators:
                operators[op['rarity']].append(op['name'])

            else:
                operators[op['rarity']] = [op['name']]
        result += f"\n推荐tag：{'+'.join(tags_info)}\n"
        for rarity in range(1, 7):
            if rarity in operators:
                result += f"{'★' * rarity}: {', '.join(operators[rarity])}\n"

    return result


async def preprocess_tags(taglist: List[str]) -> List[str]:
    for idx, tag in enumerate(taglist):
        if "术师" in tag:
            taglist[idx] = tag.replace("术师", "术士")

        if tag in {'近卫', '重装', '先锋', '医疗', '辅助', '特种', '术士', '狙击'}:
            taglist[idx] = f"{tag}干员"
        if tag in {"高资", "高姿", "高级"}:
            taglist[idx] = "高级资深干员"
        if tag in {"资深", "资干"}:
            taglist[idx] = "资深干员"
        if tag in {"快活", "复活"}:
            taglist[idx] = "快速复活"
        if tag in {"近战", "地面"}:
            taglist[idx] = "近战位"
        if tag in {"远程", "高台"}:
            taglist[idx] = "远程位"
        if tag in {"费回", "回费", "费用恢复", "费恢"}:
            taglist[idx] = "费用回复"
        if tag in {"机械", "小车"}:
            taglist[idx] = "支援机械"
        if tag in {"男性", "男", "男人"}:
            taglist[idx] = "男性干员"
        if tag in {"女性", "女", "女人"}:
            taglist[idx] = "女性干员"

    taglist = [_ for _ in taglist if _ in TAGS]
    if len(taglist) > 5:
        taglist = taglist[:5]

    return taglist
