## Jobs

# intro : get Element in List 
a = [1,2,3,4,5,6,7,8,9]

a[1] # 2
a[0:5] # 1,2,3,4,5
a[1:] # 2,3,4,5,6,7,8,9
a[1:-1] # 2,3,4,5,6,7,8

#Basic Structure
import requests
from bs4 import BeautifulSoup

# URL of Site for scrapping
url = 'https://weworkremotely.com/categories/remote-full-stack-programming-jobs'

# Test Connection
response = requests.get(url)

# use BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

jobs = soup.find("section", class_="jobs")
list = jobs.find_all("li", class_="new-listing-container")

for job in list:
    title = job.find('h3', class_="new-listing__header__title").text
    company = job.find('p', class_="new-listing__company-name").text

    print(f"{title} ----- {company}")
