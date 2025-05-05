from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_sso_empty_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://example.com/login')
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login with SSO')]").click()
    time.sleep(2)
    driver.find_element(By.ID, 'idSIButton9').click()
    error_msg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'error_message_id'))).text
    assert "Please enter your username and password" in error_msg
    driver.quit()
