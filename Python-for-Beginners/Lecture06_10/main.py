## Interactivity

# Base code
# from playwright.sync_api import sync_playwright
# p = sync_playwright().start()
# browser = p.firefox.launch(headless = False)

# page = browser.new_page()
# page.goto("https://google.com")
# page.screenshot(path="screenshot.png")

# Result Code
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()
browser = p.firefox.launch(headless=False)

page = browser.new_page()
# change website address
page.goto("https://www.wanted.co.kr/")
# set a interval for loading
time.sleep(5)

# select object by using class
page.click('button.wds-1cqc7gt')

time.sleep(5)
# select object by using placeholder text
page.get_by_placeholder("검색어를 입력해 주세요.").fill("Flutter")

time.sleep(5)

page.keyboard.down('Enter')
time.sleep(5)

page.click("a#search_tab_position")
time.sleep(5)

same_count = 0

# Loop for Scroll to End Page
while same_count < 3:
    height = page.evaluate("document.body.scrollHeight")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

    new_height = page.evaluate("document.body.scrollHeight")
    if new_height == height:
        same_count += 1
    else:
        same_count = 0

time.sleep(5)

content = page.content()
soup = BeautifulSoup(content, "html.parser")

p.stop()

