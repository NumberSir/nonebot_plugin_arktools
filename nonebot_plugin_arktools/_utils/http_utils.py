import httpx
from nonebot import logger


async def async_GET(url, *, retry: int = 5, **kwargs):
    async with httpx.AsyncClient() as client:
        for times in range(retry):
            try:
                return await client.get(url, **kwargs)
            except httpx.TimeoutException:
                logger.warning(f"请求第{times+1}次失败...")
                continue
            except Exception:
                raise
        raise
