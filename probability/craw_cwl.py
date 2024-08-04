import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import os


# Initialize WebDriver (e.g., Chrome)
driver = webdriver.Chrome()  # Adjust as needed
print("WebDriver initialized")

# Function to scrape a page and return content
def scrape_page(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Extract desired content, example extracting all paragraphs
    content = [p.get_text() for p in soup.find_all('p')]
    return content

# Function to click all links and scrape
def click_and_scrape_links(driver):
    links = driver.find_elements(By.TAG_NAME, 'a')
    data = {}
    link_data = [(link.get_attribute('href'), link.text.strip()) for link in links if link.get_attribute('href') and link.text.strip()]
    # Loop through the list of links
    for i, (href, link_text) in enumerate(link_data):
        print(f"Clicking link {i+1}/{len(link_data)}: {link_text}")
        driver.get(href)
        time.sleep(5)  # Wait for the page to load
        print(f"Scraping content from {link_text}")
        page_content = scrape_page(driver)
        data[link_text] = page_content
        driver.back()
        time.sleep(5)  # Wait for the previous page to load
    return data


def establish_connection(main_url):
    # Main script
    print("Navigating to the main page")
    # Navigate to the main page
    driver.get(main_url)

def get_page():
    #scrape the whole page
    with open('lotteries.txt', 'w', encoding='utf-8') as f:
        body = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]')
        f.write(body.text + '\n\n')
        
        


establish_connection('https://cwlottery.com/c/2022/12/30/525905.shtml')
get_page()
