from unittest.result import failfast
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

# Enviroments
timer = 2
chrome = r'/Users/adamslapaix/Documents/drivers/chromedriver'
baseUrl = 'https://demoqa.com/text-box'
msgError = "Tu elemento no se visualiza"
msgFatalError = "No se encuentra el elemento"
# setUp

driver = webdriver.Chrome(chrome)
driver.maximize_window()
driver.get(baseUrl)
time.sleep(timer)

# Se pueden hacer combinaciones al usar la condicional if, usando el try catch el try catch validara que encuentre el elemento y el if si es elemento
# Esta habilidtado
try:
    button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='submit']")))
    driver.execute_script("arguments[0].scrollIntoView();", button)
    button = driver.find_element(By.XPATH, "//button[@id='submit']")
    # El if dice si esta enable y para saber si es true a lo quede ser podemos imprimir el button.is_enabled(), si es verdadero
    if(button.is_enabled()==True):
        button.click()
        time.sleep(timer)
    else:
        print(msgError)

except TimeoutException as ex:
    print(ex.msg)
    print(msgFatalError)

driver.close()

