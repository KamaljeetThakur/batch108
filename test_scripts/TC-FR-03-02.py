from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_invalid_pro_number_filter():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://example.com/dataset')
    driver.find_element(By.ID, 'pro_number').send_keys('invalidPRO')
    driver.find_element(By.ID, 'filter_button').click()
    error_msg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'no_results_id'))).text
    assert "No results found" in error_msg
    driver.quit()
