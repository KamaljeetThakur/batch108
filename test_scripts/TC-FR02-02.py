from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Test for invalid input during needs assessment
def test_invalid_input_needs_assessment():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/login")
        # Log in step
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("valid_user")
        driver.find_element(By.ID, "password").send_keys("ValidPassword!")
        driver.find_element(By.ID, "login").click()
        # Navigate to assessment page
        WebDriverWait(driver, 10).until(EC.url_contains("/needs-assessment"))
        driver.find_element(By.ID, "customerSelect").click()
        driver.find_element(By.XPATH, "//option[text()='Customer 1']").click()
        # Fill out needs assessment with invalid characters
        driver.find_element(By.ID, "needsInput").send_keys("!")
        driver.find_element(By.ID, "submitButton").click()
        assert driver.find_element(By.ID, "errorMessage").is_displayed()
        assert driver.find_element(By.ID, "errorMessage").text == "Invalid input detected."
    finally:
        driver.quit()
