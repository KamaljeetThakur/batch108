from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    start_time = time.time()
    driver.get("http://example.com/login")
    driver.find_element(By.ID, "username").send_keys("validUser")
    driver.find_element(By.ID, "password").send_keys("validPass")
    driver.find_element(By.ID, "loginButton").click()
    driver.find_element(By.ID, "customerInteractionPage")
    load_time = time.time() - start_time
    assert load_time < 3
    print("Test case passed: Page loaded within acceptable time.")
except Exception as e:
    print(f"Test case failed: {e}")
finally:
    driver.quit()