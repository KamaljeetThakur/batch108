from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Test for empty message interaction
def test_empty_message_interaction():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/login")
        # Log in step
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("valid_user")
        driver.find_element(By.ID, "password").send_keys("ValidPassword!")
        driver.find_element(By.ID, "login").click()
        # Navigate to interaction page
        WebDriverWait(driver, 10).until(EC.url_contains("/interaction"))
        driver.find_element(By.ID, "startChat").click()
        # Attempt to send an empty message
        driver.find_element(By.ID, "sendButton").click()
        assert driver.find_element(By.ID, "errorMessage").is_displayed()
        assert driver.find_element(By.ID, "errorMessage").text == "Cannot send an empty message."
    finally:
        driver.quit()
