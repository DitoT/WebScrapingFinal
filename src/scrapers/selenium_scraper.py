from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_indeed_dynamic(query="data analyst", location="New York", limit=1000):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/118.0.5993.71 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/118.0.5993.71 Safari/537.36"
    })

    url = f"https://www.indeed.com/jobs?q={query}&l={location}"
    job_list = []

    try:
        driver.get(url)
        time.sleep(7)

        cards = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")

        for card in cards[:limit]:
            try:
                title = card.find_element(By.CLASS_NAME, "jobTitle").text
            except:
                title = None
            try:
                company = card.find_element(By.CLASS_NAME, "companyName").text
            except:
                company = None
            try:
                location = card.find_element(By.CLASS_NAME, "companyLocation").text
            except:
                location = None
            try:
                date = card.find_element(By.CLASS_NAME, "date").text
            except:
                date = None
            try:
                salary = card.find_element(By.CLASS_NAME, "salary-snippet").text
            except:
                salary = None

            job_list.append({
                "title": title,
                "company": company,
                "location": location,
                "date_posted": date,
                "salary": salary,
                "source": "Indeed (Selenium)"
            })

        with open("indeed_debug.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

    finally:
        driver.quit()

    return job_list