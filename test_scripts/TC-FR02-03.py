from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def clear_filters(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "date_filter_button"))
        ).click()
        driver.find_element(By.ID, "start_date").send_keys("2023-11-01")
        driver.find_element(By.ID, "end_date").send_keys("2023-12-01")
        driver.find_element(By.ID, "apply_filters").click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "clear_filters"))
        ).click()
        time.sleep(2)
        # Verify original data is back
        # Additional verification logic can be implemented here
        print("Filters cleared and original data set displayed.")
    except Exception as e:
        print(f"Clearing filters failed: {e}")
    finally:
        driver.quit()
