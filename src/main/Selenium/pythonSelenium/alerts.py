from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Environments 
timer = 2
chrome = r'/Users/adamslapaix/Documents/drivers/chromedriver'
baseUrl = "https://www.udemy.com/course/pythonforbeginners/"
msgError = "Do not Found Element"

# setUp Navigation Driver
driver = webdriver.Chrome(chrome)
driver.maximize_window()

# Navigation to driver
driver.get(baseUrl)
time.sleep(timer)

# Navigation driver find elements
try:
    get = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[6]")))
    get = driver.find_element(By.XPATH, "(//button[@type='button'])[6]")

except TimeoutException as ex:
    print(ex.msg)
    print(msgError)
    driver.quit()
# Para elementos que esten declarados como aceptar, dentro los modales podemos usar el alert que sirve para
# aceptar o cerrar un modale
# Para aceptar se usa

'''
driver.switch_to.alert.accept()

# Para cerrar 
driver.switch_to.alert.dismiss()
'''
# Estos no se utilizan mucho debido a que no siempre estan declarados de manera tal.
# Tambien podemos buscar los elementos por el Xpath y hacerlo de manera canalla

# La manera correcta de ejecutar el click dentro de un modale es realizar un try cathc para que espere el 
# elemento y luego lo presione

try:
    get = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Ir a la cesta')]")))
    get = driver.find_element(By.XPATH, "//span[contains(text(), 'Ir a la cesta')]").click()
    time.sleep(timer)

except TimeoutException as ex:
    print(ex.msg)
    print(msgError)
    driver.quit()

# TearDown
driver.close()