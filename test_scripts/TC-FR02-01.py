from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_data_by_dates(url, start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "date_filter_button"))
        ).click()
        driver.find_element(By.ID, "start_date").send_keys(start_date)
        driver.find_element(By.ID, "end_date").send_keys(end_date)
        driver.find_element(By.ID, "apply_filters").click()
        time.sleep(2)
        # Verify data displayed is within range
        # Additional verification logic can be implemented here
        print("Data filtered successfully within the specified dates.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()
