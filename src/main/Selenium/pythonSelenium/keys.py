from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/Users/adamslapaix/Documents/drivers/chromedriver")
driver.maximize_window()
driver.get("https://demoqa.com/")
time.sleep(1)
driver.get("https://www.google.com")
time.sleep(1)
# back sirve para para volver a la pagina de atras, pero hay que saber que la funcion back tiene un tiempo limite siempre y cuando
# no pasen mas de 3 segundos volvera.
# driver.back()

# Para que no falle por tiempo debemos ejecjutar una funcion de javascript la cual vamos a indicar cuantas paginas atras queremos que vuelva

driver.execute_script("window.history.go(-1)")
# si marcamos un -2 volvera dos paginas atras
# Usar la funcion de javascript es mejor ya que por tiempo no dara error

# Para avanzar hacia delante usamos foward

# driver.forward()
# Pero al usar esta funcion de Selenium se limita por el tiempo

# debemos usar la funcion de javascript pero en positivo

driver.execute_script("window.history.go(1)")
time.sleep(2)
 