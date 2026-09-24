## BeautifulSoup

import requests
from bs4 import BeautifulSoup

# URL of Site for scrapping
url = 'https://weworkremotely.com/categories/remote-full-stack-programming-jobs'

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

jobs = soup.find("section",class_="jobs").find_all("li")[0:-1]

for job in jobs:
    title = job.find('h3','new-listing__header__title').text
    companies = job.find_all("p","new-listing__categories__category")
    for idx in range(len(companies)):
        company_within = companies[idx].text
        print(title,"-----------",company_within)