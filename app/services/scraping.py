# Loading necessary packages

from playwright.sync_api import sync_playwright
import json


KEYCAP_URL = "https://keeb-finder.com/keycaps"
SWITCH_URL = "https://keeb-finder.com/switches"
LUBRICANT_URL = "https://keeb-finder.com/accessories/lubrications"
KIT_URL = "https://keeb-finder.com/keyboards"


with sync_playwright() as kc:

    browser = kc.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(KEYCAP_URL)
    print(page.content())

    kc_data = []
    keycaps = page.query_selector_all('.product-card')

    for keycap in keycaps:
        name = keycap.query_selector("h3").inner_text()
        description = keycap.query_selector("p").inner_text()
        price = keycap.query_selector("span.price").inner_text()
        
        kc_data.append({
            "name": name,
            "description": description,
            "price": price
        })

    browser.close()

    with open('app/services/keycaps.json', 'w') as f:
        json.dump(kc_data, f, indent=4)