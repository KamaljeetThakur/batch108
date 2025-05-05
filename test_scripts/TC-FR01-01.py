from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com')
    assert 'Homepage' in driver.title
    driver.find_element(By.XPATH, "//button[contains(text(), 'Interact with Customers')]").click()
    time.sleep(2)
    assert 'Customer Interaction' in driver.title
    print("Customer interaction platform is accessible.")
finally:
    driver.quit()