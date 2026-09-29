## Pagination

import requests
from bs4 import BeautifulSoup

all_jobs=[]

# Create new Function for handling page
def scrap_page(url):

    # Copy previous structure
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find("section", class_="jobs")
    list = jobs.find_all("li", class_="new-listing-container")

    for job in list:
        title = job.find('h3', class_="new-listing__header__title").text
        company = job.find('p', class_="new-listing__company-name").text
        headquater = job.find('p', class_="new-listing__company-headquarters")
        
        headquater_text = ""
        if headquater :
            headquater_text = f"({headquater.text})"
        else:
            headquater_text = ""
        
        print(f"{title} - {company}{headquater_text}")

import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/remote-full-time-jobs?page=2"
response = requests.get(url) 
soup = BeautifulSoup(response.content, "html.parser")

pages = soup.find('div', class_="pagination")
buttons = len(pages.find_all("span", class_="page"))
print(buttons)
