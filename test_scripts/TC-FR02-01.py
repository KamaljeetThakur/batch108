from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/customer-interaction')
    assert 'Customer Interaction' in driver.title
    driver.find_element(By.XPATH, "//button[contains(text(), 'Identify Customer Needs')]").click()
    time.sleep(1)
    driver.find_element(By.ID, 'customerData').send_keys('Example Data')
    driver.find_element(By.ID, 'submitButton').click()
    time.sleep(2)
    assert 'Needs Identified' in driver.page_source
    print("Customer needs identification tool works successfully.")
finally:
    driver.quit()