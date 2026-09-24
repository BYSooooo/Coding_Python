## BeautifulSoup

import requests
from bs4 import BeautifulSoup

# URL of Site for scrapping
url = 'https://weworkremotely.com/categories/remote-full-stack-programming-jobs'

# Test Connection
response = requests.get(url)
print(response.content)

# use BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

jobs = soup.find("section", class_="jobs")
list = jobs.find_all("li", class_="new-listing-container")

for job in list:
    title = job.find('h3', class_="new-listing__header__title").text
    shape = ""
    categories = job.find_all('p', class_="new-listing__categories__category")
    for idx in range(len(categories)):
        within = categories[idx].text
        shape = shape + within

    print(title, "------", shape)