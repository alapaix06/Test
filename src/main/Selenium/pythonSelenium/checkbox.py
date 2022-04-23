from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://endtest.io/guides/docs/how-to-test-checkboxes/")
driver.maximize_window()

# Para realizar checkbox, lo que tenemos que hacer es click en elemento usando un explicit wait

checkbox1 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pet1"]')))
checkbox1.click()

checkbox2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'pet3')]")))
checkbox2.click()

time.sleep(2)

driver.close()
