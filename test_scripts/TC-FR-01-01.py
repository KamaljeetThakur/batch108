from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_sso_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://example.com/login')
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login with SSO')]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'i0116'))).send_keys('valid_username')
    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'i0118'))).send_keys('valid_password')
    driver.find_element(By.ID, 'idSIButton9').click()
    assert "Dashboard" in driver.title
    driver.quit()
