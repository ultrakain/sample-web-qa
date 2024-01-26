from selenium import webdriver
import requests
from selenium.webdriver.chrome.service import Service


def check_url_status(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        current_url = driver.current_url
        response = requests.get(current_url)
        status_code = response.status_code
        return status_code
    finally:
        driver.quit()


def test_url_status():
    url_to_check = "https://www.dodopoint.com/"
    status_code = check_url_status(url_to_check)
    assert status_code == 200, f"Expected status code 200, but got {status_code}"

# Run the test using pytest in the terminal
# pytest test_url_status.py
