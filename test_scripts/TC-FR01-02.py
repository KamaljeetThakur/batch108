from selenium import webdriver
import os
import time
from selenium.common.exceptions import WebDriverException

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)
try:
    driver.get('http://example.com')
    time.sleep(5)  # Simulate offline condition
    assert 'Cannot connect to the Internet' in driver.page_source
    print("Error message displayed when offline.")
finally:
    driver.quit()