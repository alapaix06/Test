from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
# Esta es la libreria para hacer los exceptions 
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Firefox(executable_path=r'/Users/adamslapaix/Documents/drivers/geckodriver')

driver.get('https://breakawayprep.com/register-practice-test/')
driver.maximize_window()
time.sleep(2)

# la funicion try catch es una funcion que se ejecuta y si hay un error se ejecuta el except
# el except es el que se ejecuta si hay un error

# Para seleccionar un elemento con Try debemos hacer un explicity wait para que espere el elemento, 
# Lo que hacemos es decirle que busque dentro

#  Tenemos el try catch con finally que sirve para que ejecute un funcion y termine
try:
    selectCountry = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,
     "//select[@name='SelectaLocation']")))
    selectC = Select(selectCountry)
    selectC.select_by_index(2)
    time.sleep(10)

    selectDate = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,
     "//select[contains(@name,'selectdate')]")))
    selectD = Select(selectDate)
    selectD.select_by_index(3)
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
finally:
    # quit sirve para cerrar todas las ventanas del navegador
    driver.quit()


# Para que hagamos un try catch que valide si esta y continue debemos usar except con la libreria 
# TimeoutException

# Para esto debemos importar la libreria y utilizar except por finally

try:
    selectCountry = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,
     "//select[@name='SelectaLocation']")))
    selectC = Select(selectCountry)
    selectC.select_by_index(2)

# Se usa el except para que cuando falle el try haga lo del except y continue con lo demas
except TimeoutException as ex:
    # Le decimos que imprima el ex que es el TimeoutExeption con el msg
    print(ex.msg)
    print("Don't found element")

driver.execute_script("window.scrollTo(0,250)")
driver.find_element(By.XPATH, "//input[@name='StudentName']").send_keys("Adams")
time.sleep(2)

driver.close()