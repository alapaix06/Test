# El explicity wait sirve para esperar un elemento en especial 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Estas son las dos librerias que debemos usar para que el explicity wait funcione
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path=r'/Users/adamslapaix/Documents/drivers/chromedriver')
driver.get('')
driver.maximize_window()

# El explicity wait sirve para esperar un elemento en especial, para poder implementarlo necesitamos importar la libreria de WebDriverWait, debemos
# usar los diferentes elementos del explicity
# ej: primero declaramos una varibale al igual que cualquier objeto


# WebDriverWait sirve para llamar la libreria, dentro de este llamamos el driver y luego indicamos los segundos que va a esperar dicho elemento
# El EC llama la libreria y el element hace referencia que pasara cuando espere un elemento.
# El until sirve para validar que los elementos dentro del driver cumple la condicion 

button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.XPATH, "//a[containts(text(),'test')]"))
button.click()

