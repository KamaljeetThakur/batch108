from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_customer_interaction():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com")
        driver.find_element(By.XPATH, "//a[text()='Interact with Customers']").click()
        assert "Customer Interaction" in driver.title
        print("Successful access to customer interaction platform")
    finally:
        driver.quit()
