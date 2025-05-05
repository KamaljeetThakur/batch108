from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_data_invalid_dates(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "date_filter_button"))
        ).click()
        driver.find_element(By.ID, "start_date").send_keys("2023-12-01")
        driver.find_element(By.ID, "end_date").send_keys("2023-11-01")
        driver.find_element(By.ID, "apply_filters").click()
        time.sleep(2)
        no_results_message = driver.find_element(By.ID, "no_results").text
        assert no_results_message == "No results found"
        print("Received no results message for invalid date range.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()
