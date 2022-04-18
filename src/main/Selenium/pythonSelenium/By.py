from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Tambien debemos importar el By que sirve para encontrar elementos
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r'/Users/adamslapaix/Documents/drivers/chromedriver')
driver.maximize_window()

driver.get("https://demoqa.com/text-box")

driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("Klk loco")

driver.execute_script("window.scrollTo(0,300)")

# Aqui solo debemos usar find_element, luego el By.por el cual buscaremos, luego usamos coma para luego indicar que buscara
driver.find_element(By.ID, "submit").click()
time.sleep(2)
driver.close()