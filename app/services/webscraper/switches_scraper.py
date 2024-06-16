# Loading necessary packages

from playwright.sync_api import sync_playwright
import json


KEYCAP_URL = "https://keeb-finder.com/keycaps"
LUBRICANT_URL = "https://keeb-finder.com/accessories/lubrications"
KIT_URL = "https://keeb-finder.com/keyboards"


for pages in range(1, 21, 1):

    SWITCH_URL = f"https://keeb-finder.com/switches?ms_inStock=In+Stock&page={pages}"

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(SWITCH_URL)

        data = []
        for i in range(1, 25, 1):
            name = page.query_selector(f'body > div.flex.flex-wrap.justify-center > div.max-w-lg.w-full.px-4.my-2.z-0 > div.grid.gap-4.grid-cols-2.xs\:grid-cols-2.sd\:grid-cols-3.lg\:grid-cols-4 > article:nth-child({i}) > \
                                    div.flex.flex-wrap.items-center.justify-between.mt-1.mb-1\.5.group > a.font-h4.text-h4.text-gray-900.dark\:text-gray-100.p-1.text-left.cursor-pointer.webkit-box.overflow-hidden.no-underline.line-clamp-2').inner_text()
            price = page.query_selector(f'body > div.flex.flex-wrap.justify-center > div.max-w-lg.w-full.px-4.my-2.z-0 > div.grid.gap-4.grid-cols-2.xs\:grid-cols-2.sd\:grid-cols-3.lg\:grid-cols-4 > article:nth-child({i}) > \
                                        div.aspect-\[1\/1\].relative.w-full.overflow-hidden.rounded-lg.bg-gray-200.undefined > div.absolute.right-1\.5.bottom-1\.5.flex.justify-end.bg-black.bg-opacity-70.p-1\.5.px-2.rounded.text-center.z-10.text-gray-100.font-medium').inner_text()
            
            data.append({
                "name": name,
                "price_per_unit": price
            })

        browser.close()

        with open('app/services/webscraper/data/switches.json', 'a') as f:
                json.dump(data, f, indent=4)


