from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_customer_interaction_edge():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com")
        message = driver.find_element(By.ID, "no_customers").text
        assert message == "No customers available"
        print("Correct message shown when no customers present")
    finally:
        driver.quit()
