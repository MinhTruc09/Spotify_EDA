from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time,random,pandas as pd


service = Service("chromedriver.exe")
opts = Options()
opts.add_argument("--disable-blink-features=AutomationControlled")
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36")
driver = webdriver.Chrome(service=service, options=opts)

def scrape_spotify_chart(url):
    driver.get(url)
    time.sleep(random.uniform(2,4))
    # nút download csv 
    