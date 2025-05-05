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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "customerNeedsPage")))
    driver.find_element(By.ID, "startAssessment").click()
    driver.find_element(By.ID, "customerData").send_keys("John Doe, 30, Tech-savvy")
    driver.find_element(By.ID, "submitAssessment").click()
    needs_summary = driver.find_element(By.ID, "summary").is_displayed()
    assert needs_summary == True
    print("Test case passed: Needs summary generated successfully.")
except Exception as e:
    print(f"Test case failed: {e}")
finally:
    driver.quit()