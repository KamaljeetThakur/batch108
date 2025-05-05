from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_needs_identification_no_input():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://customer-needs-assessment.com")
        assert "Needs Assessment" in driver.title
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, "error-message").text
        assert "Please answer the questions" in error_message
        print("Error message displayed as expected.")
    finally:
        driver.quit()
