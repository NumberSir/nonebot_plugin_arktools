import json


async def get_operator_data():
    with open("../_data/level.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    stars = [1, 2, 3, 4, 5, 6]
    for idx, star in stars:



if __name__ == "__main__":
    import asyncio
    from pprint import pprint
    rst = asyncio.run(get_operator_data())
    pprint(rst)