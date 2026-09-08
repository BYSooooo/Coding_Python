## Status Codes

# Base Code
from requests import get

# List of Websites
websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

# Get Response from websites
for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    print(response)


# Get Response Status Code from websites
for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response2 = get(website)
    print(response2.status_code)

# Add different message by Status Code
for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response3 = get(website)
    if response3.status_code == 200:
        print(f"{website} is OK")
    else:
        print(f"{website} not Ok")

# Apply Dictionary
result = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response4 = get(website)
    if response4.status_code == 200:
        result[website] = "OK"
    else:
        result[website] = "FAILED"

print(result)

