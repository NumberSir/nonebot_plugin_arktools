from typing import Optional
from playwright.async_api import Browser, async_playwright
import nonebot
from nonebot import Driver
from nonebot.log import logger
import base64


driver: Driver = nonebot.get_driver()


_browser: Optional[Browser] = None


async def init(**kwargs) -> Optional[Browser]:
    global _browser
    try:
        browser = await async_playwright().start()
        _browser = await browser.chromium.launch(**kwargs)
        return _browser
    except NotImplementedError:
        logger.warning("win环境下 初始化playwright失败，相关功能将被限制....")
    except Exception as e:
        logger.warning(f"启动chromium发生错误 {type(e)}：{e}")
        if _browser:
            await _browser.close()
    return None


async def get_browser(**kwargs) -> Browser:
    return _browser or await init(**kwargs)


async def get_dynamic_screenshot(url):
    browser = await get_browser()
    page = None
    try:
        page = await browser.new_page(device_scale_factor=2)
        await page.goto(url, wait_until="networkidle", timeout=50000)
        await page.set_viewport_size({"width": 2560, "height": 1080})
        card = await page.query_selector(".card")
        assert card
        clip = await card.bounding_box()
        assert clip
        bar = await page.query_selector(".text-bar")
        assert bar
        bar_bound = await bar.bounding_box()
        assert bar_bound
        clip["height"] = bar_bound["y"] - clip["y"]
        image = await page.screenshot(clip=clip, full_page=True)
        await page.close()
        return base64.b64encode(image).decode()
    except Exception:
        if page:
            await page.close()
        raise


# @driver.on_startup
def install():
    """自动安装、更新 Chromium"""
    logger.info("正在检查 Chromium 更新")
    import sys
    from playwright.__main__ import main

    sys.argv = ["", "install", "chromium"]
    try:
        main()
    except SystemExit:
        pass
