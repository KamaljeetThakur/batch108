from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_customer_needs_identification_invalid():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://customer-needs-url")
 driver.find_element(By.ID, "customerField").send_keys("Invalid Details")
 assert "Invalid customer details" in driver.page_source
 print("Test Passed: Correctly handled invalid customer input.")
 finally:
 driver.quit()
