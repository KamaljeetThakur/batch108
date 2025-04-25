from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_identify_needs_error():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/needs-identification")
        driver.find_element(By.ID, "customer_data").send_keys("")
        driver.find_element(By.ID, "identify_needs").click()
        error_message = driver.find_element(By.ID, "error").text
        assert error_message == "Invalid data provided"
        print("Correctly shows error for invalid input")
    finally:
        driver.quit()
