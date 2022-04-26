from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r'/Users/adamslapaix/Documents/drivers/chromedriver')
baseUrl = 'https://github.com/'
temp = 3
msgCount = "los campos son: "



driver.get(baseUrl)
driver.maximize_window()
time.sleep(temp)

# Para encontrar todos los links de una pagina usamos el find_elements que sirve para encontrar multiples elementos y buscamos por el tag_name
# El find_elements busca distintos valores
# El Tag_name es el nombre de la etiqueta que busca
links =driver.find_elements(By.TAG_NAME, "a")
# Len es para contar los valores que encontro en links
print(msgCount, len(links))

# Podemos listar todos los links de una pagina usando la funcion for 

# Con este for decimos que los valores de links lo pasamos a difLinks 
for difLinks in links:
    # el .text sirve para listar los valores en textos
    print(difLinks.text)


# Podemos encontrar los links por sus textos usando la funcion find_element_by_text_link
# Y asi accede
driver.find_element_by_link_text("Shop").click()
time.sleep(temp)



