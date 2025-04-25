from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_identify_needs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/needs-identification")
        driver.find_element(By.ID, "customer_data").send_keys("Customer data example")
        driver.find_element(By.ID, "identify_needs").click()
        assert "Needs Identified" in driver.page_source
        print("Customer needs identified successfully")
    finally:
        driver.quit()
