from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_customer_interaction_error():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com")
        driver.find_element(By.XPATH, "//a[text()='Interact with Customers']").click()
        error_message = driver.find_element(By.ID, "error").text
        assert error_message == "Please login first"
        print("Error message displayed correctly for unauthorized access")
    finally:
        driver.quit()
