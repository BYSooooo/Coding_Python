## Exporting to Excel

# Base Structure
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

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

jobs = soup.find_all('div', class_="JobCard_container__zQcZs")

jobs_db = []

for job in jobs:
    link = f"https://wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title___kfvj").text
    company_name = job.find("span", class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu wds-nkj4w6").text
    reward = job.find("span", class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__location__4_w0l wds-nkj4w6").text

    job = {
        "title" : title,
        "company_name" : company_name,
        "reward" : reward,
        "link" : link
    }
    jobs_db.append(job)


# Convert to CSV
import csv

file = open("jobs.csv", "w")
writer = csv.writer(file)

# New Row - Key
writer.writerow(["Title", "Company", "Reward", "Link"])
# Add Rows - get Datas
for job in jobs_db:
    writer.writerow(job.values())

file.close()