import requests
from bs4 import BeautifulSoup
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
PROXIES = [
    "http://200.25.254.193:54240",
    "http://45.167.125.97:9992",
    "http://103.169.255.10:3127",
    "http://185.189.199.75:23500",
    "http://103.151.20.133:80",
    "http://103.167.34.3:8080"
]


def get_random_proxy():
    return {"http": random.choice(PROXIES), "https": random.choice(PROXIES)}

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/92.0.4515.159 Safari/537.36"
]


def scrape_remoteok_jobs(limit=1000):
    url = "https://remoteok.com/api"
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    job_list = []

    time.sleep(random.uniform(1.5, 3.0))
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        return []

    data = response.json()[1:]
    for job in data[:limit]:
        job_list.append({
            "title": job.get("position"),
            "company": job.get("company"),
            "location": job.get("location") or "Remote",
            "date_posted": job.get("date") or job.get("posted_at"),
            "salary": job.get("salary") or "N/A",
            "source": "RemoteOK"
        })

    return job_list

def scrape_wwr_jobs(limit=10):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/118.0.5993.71 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/118.0.5993.71 Safari/537.36"
    })

    url = "https://weworkremotely.com/categories/remote-programming-jobs"
    job_list = []

    try:
        driver.get(url)
        time.sleep(5)

        cards = driver.find_elements(By.CLASS_NAME, "job")

        count = 0
        for card in cards:
            if count >= limit:
                break
            try:
                title = card.find_element(By.CLASS_NAME, "title").text
            except:
                title = None
            try:
                company = card.find_element(By.CLASS_NAME, "company").text
            except:
                company = None
            try:
                location = card.find_element(By.CLASS_NAME, "region").text
            except:
                location = "Remote"

            job_list.append({
                "title": title,
                "company": company,
                "location": location,
                "date_posted": "N/A",
                "salary": "N/A",
                "source": "WeWorkRemotely (Selenium)"
            })

            count += 1

    finally:
        driver.quit()

    return job_list