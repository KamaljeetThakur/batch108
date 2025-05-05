from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_required_for_interaction():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://customer-interaction-platform.com")
        assert "Customer Interaction" in driver.title
        driver.find_element(By.XPATH, "//button[text()='Start Interaction']").click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, "error-message").text
        assert "Please log in" in error_message
        print("Error message displayed as expected.")
    finally:
        driver.quit()
