from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_invalid_interaction_platform():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://invalid-url")
 assert "Page Not Found" in driver.page_source
 print("Test Passed: Correctly handled invalid URL.")
 finally:
 driver.quit()
