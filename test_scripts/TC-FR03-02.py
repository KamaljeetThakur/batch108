from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_invalid_pro_number(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "filter_button"))
        ).click()
        driver.find_element(By.ID, "criteria_contains").click()
        driver.find_element(By.ID, "pro_number_input").send_keys("INVALID123")
        driver.find_element(By.ID, "apply_filter").click()
        time.sleep(2)
        no_results_message = driver.find_element(By.ID, "no_results").text
        assert no_results_message == "No results found"
        print("Received no results message for an invalid PRO Number.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()
