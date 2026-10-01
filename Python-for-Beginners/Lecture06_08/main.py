## Playwright

# Install Playwright
# pip install playwright

from playwright.sync_api import sync_playwright

# Playwright Start
p = sync_playwright().start()
# Firefox Browser launching
browser = p.firefox.launch()
# set a New page
page = browser.new_page()

# Move to Google
page.goto("https://google.com")
# Take screenshot
page.screenshot(path="screenshot.png")

# Turn off headless mode
p_2 = sync_playwright().start()
browser_2 = p_2.firefox.launch(headless=False)
page_2 = browser_2.new_page()

page_2.goto("https://google.com")
page_2.screenshot(path="screenshot2.png")