from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_date_filtering():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://example.com/data-filter')
    driver.find_element(By.ID, 'start_date').send_keys('2023-01-01')
    driver.find_element(By.ID, 'end_date').send_keys('2023-12-31')
    driver.find_element(By.ID, 'filter_button').click()
    assert "Filtered Results" in driver.page_source
    driver.quit()
