## Collection Job

# Base Structure
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()
browser = p.firefox.launch(headless=False)

page = browser.new_page()
page.goto("https://www.wanted.co.kr/")
time.sleep(5)

page.click('button.wds-1cqc7gt')
time.sleep(5)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("Flutter")
time.sleep(5)

page.keyboard.down('Enter')
time.sleep(5)

page.click("a#search_tab_position")
time.sleep(5)

same_count = 0

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
p.stop()

soup = BeautifulSoup(content, "html.parser")

# Get a Job List
jobs = soup.find_all('div', class_="JobCard_container__zQcZs")

for job in jobs:
    anchor = job.find("a")