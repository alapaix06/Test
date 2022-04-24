from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


driver = webdriver.Chrome(executable_path=r'/Users/adamslapaix/Documents/drivers/chromedriver')


driver.get('https://testingqarvn.com.es/upload-files/')
driver.execute_script("window.scrollTo(0,1000)")
time.sleep(2)

# usamos el upload file para que el try valide ya que siempre lo hara con la primera funcion que haya
try:
    # Este upload sirve para encontrar el elemento
    uploadfile = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'wsf-1-field-94')]")))
    # Para subir un archivo debemos enviar la ruta del elemento para enviarla
    sendfile = driver.find_element(By.XPATH, "//input[contains(@id,'wsf-1-field-94')]")
    sendfile.send_keys("/Users/adamslapaix/Downloads/name.png")
    time.sleep(3)
    
except TimeoutException as ex:
    print("Do not found element")

driver.close()