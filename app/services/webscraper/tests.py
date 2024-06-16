from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://keeb-finder.com/switches?ms_inStock=In+Stock")
body > div.flex.flex-wrap.justify-center > div.max-w-lg.w-full.px-4.my-2.z-0 > div.MuiBox-root.mui-0 > nav > ul > li:nth-child(8) > a