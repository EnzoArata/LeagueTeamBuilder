from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import time
import random

def update_champion_data(lane):
    top_url = "https://www.op.gg/champions?position=top"
    jg_url = "https://www.op.gg/champions?position=jungle"
    mid_url = "https://www.op.gg/champions?position=mid"
    bot_url = "https://www.op.gg/champions?position=adc"
    support_url = "https://www.op.gg/champions?position=support"

    # Configure Chrome options for a headless browser
    chrome_options = Options()

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        # Add more user agents if needed
    ]
    chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled") 
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    chrome_options.add_experimental_option("useAutomationExtension", False) 

    # Path to your Chrome WebDriver
    current_directory = os.path.dirname(os.path.realpath(__file__))
    webdriver_path = os.path.join(current_directory, "chromedriver")

    driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)

    # Load the webpage
    if lane == "top":
        download_page_contents(driver, top_url,"top")
    elif lane == "jg":
        download_page_contents(driver, jg_url,"jg")
    elif lane == "mid":
        download_page_contents(driver, mid_url,"mid")
    elif lane == "bot":
        download_page_contents(driver, bot_url,"bot")
    elif lane == "sup":
        download_page_contents(driver, support_url,"sup")
    driver.quit()


def download_page_contents(driver, url, lane):
    driver.get(url)
    time.sleep(4)
    # Get the page source after JavaScript has rendered the page
    page_source = driver.page_source
    with open(f"data/{lane}.html", "w", encoding="utf-8") as file:
        file.write(page_source)