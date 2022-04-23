from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Esta libreria sirve para importar el select ya que este no funciona sin la libreria
from selenium.webdriver.support.ui import Select
import time

# Para seleccionar dentro de un combolist debemos declarar una varibale que busque el elemento
# Luego usamos el Select dentro de esa variable para seleccionar un campo

driver = webdriver.Chrome(
    executable_path=r'/Users/adamslapaix/Documents/drivers/chromedriver')

driver.maximize_window()

driver.get('https://breakawayprep.com/register-practice-test/')

selectLocation = driver.find_element(
    By.XPATH, "//select[contains(@name,'SelectaLocation')]")

# Debemos crear otra variable que le daremos el valor del select
# Aqui declaramos la variabale slc y le decimos que tome el valor de la libreria Select y este valor
# Estara seteado con la variable selectLocation
slc = Select(selectLocation)

# Luego aqui decimos que vamos a seleccionar un elemento por el index que seria el elemento 2
# Debemos tomar en cuenta que en programacion se incia en 0 
slc.select_by_index(2)
time.sleep(2)

# Tambien podemos encontrar elementos por nombre, por valor por diferentes elementos

slc.select_by_visible_text("NJ")
slc.deselect_by_value("Yesterday")

driver.close()
