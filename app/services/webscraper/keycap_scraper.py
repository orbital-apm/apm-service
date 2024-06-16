from playwright.sync_api import sync_playwright
import json

KEYCAP_URL = "https://keeb-finder.com/keycaps"
SWITCH_URL = "https://keeb-finder.com/switches"
LUBRICANT_URL = "https://keeb-finder.com/accessories/lubrications"
KIT_URL = "https://keeb-finder.com/keyboards"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(KEYCAP_URL)

    data = []
    for i in range(1, 25, 1):
        name = page.query_selector(f'body > div.flex.flex-wrap.justify-center > div.max-w-lg.w-full.px-4.my-2.z-0 > div.grid.gap-4.grid-cols-2.xs\:grid-cols-2.sd\:grid-cols-3.lg\:grid-cols-4 > article:nth-child({i}) > \
                                div.flex.flex-wrap.items-center.justify-between.mt-1.mb-1\.5.group > a.font-h4.text-h4.text-gray-900.dark\:text-gray-100.p-1.text-left.cursor-pointer.webkit-box.overflow-hidden.no-underline.line-clamp-2').inner_text()
        price = page.query_selector(f'body > div.flex.flex-wrap.justify-center > div.max-w-lg.w-full.px-4.my-2.z-0 > div.grid.gap-4.grid-cols-2.xs\:grid-cols-2.sd\:grid-cols-3.lg\:grid-cols-4 > article:nth-child({i}) > \
                                    div.aspect-\[1\/1\].relative.w-full.overflow-hidden.rounded-lg.bg-gray-200.undefined > div').inner_text()
        
        data.append({
            "name": name,
            "price": price
        })

    browser.close()

    with open('app/services/webscraper/data/keycaps.json', 'a') as f:
            json.dump(data, f, indent=4)



