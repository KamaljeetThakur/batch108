from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Test for negative interaction without login
def test_customer_interaction_without_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/interaction")
        assert "Login" in driver.title
        assert driver.find_element(By.ID, "loginMessage").is_displayed()
        assert driver.find_element(By.ID, "loginMessage").text == "Please login to continue."
    finally:
        driver.quit()
