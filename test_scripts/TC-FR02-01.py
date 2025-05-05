from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_customer_needs_identification():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://customer-needs-assessment.com")
        assert "Needs Assessment" in driver.title
        driver.find_element(By.NAME, "question1").send_keys("Service A")
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        time.sleep(2)
        assert "Thank you for your responses" in driver.page_source
        print("Needs assessment submitted successfully.")
    finally:
        driver.quit()
