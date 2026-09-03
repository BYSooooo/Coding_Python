## URL Formating

# Base Tuple
websites = (
    "google.com",
    "airbnb.com",
    "twitter.com",
    "facebook.com",
    "tictok.com"
)

# Check start with http:// , https://

# Loop websites Tuple
for website in websites:
    # Condition - website value is 'not' start with "https://"
    # if website.startswith("https://") === False
    if not website.startswith("https://"):
        # add "https://" first
        website = f"https://{website}"
        # print
        print(website)