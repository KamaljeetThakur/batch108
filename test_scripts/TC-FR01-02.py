from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get("http://example.com/login")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username"))).send_keys("validUser")
    driver.find_element(By.ID, "password").send_keys("validPass")
    driver.find_element(By.ID, "loginButton").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "customerInteractionPage")))
    driver.find_element(By.ID, "startInteraction").click()
    driver.find_element(By.ID, "interactionDetails").send_keys("")
    driver.find_element(By.ID, "submitInteraction").click()
    error_message = driver.find_element(By.ID, "error").is_displayed()
    assert error_message == True
    print("Test case passed: Error message displayed as expected.")
except Exception as e:
    print(f"Test case failed: {e}")
finally:
    driver.quit()