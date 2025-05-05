from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_heavy_load_interaction():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://customer-interaction-platform.com")
        assert "Customer Interaction" in driver.title
        # Simulating multiple interactions could require threading or another approach
        for _ in range(10):
            driver.find_element(By.XPATH, "//button[text()='Start Interaction']").click()
            time.sleep(0.5)
        print("Handled multiple interactions successfully.")
    finally:
        driver.quit()
