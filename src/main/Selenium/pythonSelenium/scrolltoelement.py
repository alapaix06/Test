from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


driver = webdriver.Chrome(executable_path=r'/Users/adamslapaix/Documents/drivers/chromedriver')


driver.get('https://testingqarvn.com.es/upload-files/')
time.sleep(2)

try:
    uploadfile = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'wsf-1-field-94')]")))
    # Para desplazarnos utilizando un elemento debemos usar la  el execute_script donde tendremos un argumento
    # que si es positivo nos mueve hacia abajo y negativo hacia arriba.
    # Aqui buscara por el uploadfile
    driver.execute_script("arguments[0].scrollIntoView();", uploadfile)
    time.sleep(3)
    
except TimeoutException as ex:
    print("Do not found element")

driver.close()