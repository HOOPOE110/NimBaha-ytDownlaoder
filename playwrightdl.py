# import os, sys

# base_path = getattr(sys, "_MEIPASS", os.path.dirname(__file__))

## ffmpeg path
# ffmpeg_path = os.path.join(base_path, "ffmpeg.exe")

## Playwright browsers path
# os.environ["PLAYWRIGHT_BROWSERS_PATH"] = os.path.join(base_path, "playwright-browsers")

import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect
import time

async def run(playwright: Playwright,link):
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://monasef.ir/")
    await page.locator("#home iframe").content_frame.get_by_role("checkbox", name="Checkbox icon. Click to").click()
    await asyncio.sleep(2)
    await page.get_by_role("textbox", name="لینک دانلود").fill(link)
    await page.get_by_role("button", name="نیم بها کن!").click()
    async with page.expect_download() as download_info:
        await page.get_by_role("button", name="بارگیری فایل").click()
    download = await (download_info.value)
    print(download.url)
    url = download.url
    return url

async def nimbahaurl(link):
    async with async_playwright() as playwright:
        url = await run(playwright,link)
        return url


# asyncio.run(nimbahaurl(link))

