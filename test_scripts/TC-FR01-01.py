from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_interaction_platform():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://customer-platform-url")
 assert "Welcome to the Customer Interaction Platform" in driver.page_source
 print("Test Passed: Interaction platform loads successfully.")
 finally:
 driver.quit()
