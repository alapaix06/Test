from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time


nameinput = "Adams"
driver = webdriver.Firefox(executable_path=r'/Users/adamslapaix/Documents/drivers/geckodriver')
driver.get('https://testingqarvn.com.es/upload-files/')
driver.maximize_window()


try:
    name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
    "//input[contains(@placeholder,'Nombre:')]")))
    driver.execute_script("arguments[0].scrollIntoView();", name)
    name = driver.find_element(By.XPATH, "//input[contains(@placeholder,'Nombre:')]")
    name.send_keys(nameinput)
    time.sleep(.5)
    
except TimeoutException as ex:
    print(ex.msg)
    print("Do not found element")
    driver.close()

lastname = driver.find_element(By.XPATH, "//input[@name='field_81']")
lastname.send_keys("Lapaix Castillo")

email = driver.find_element(By.XPATH, "//input[@name='field_82']")
email.send_keys("alapaix@testing.com")

phone = driver.find_element(By.XPATH, "//input[@name='field_83']")
phone.send_keys("8290332323")

address = driver.find_element(By.XPATH, "//textarea[contains(@id,'wsf-1-field-84')]")
address.send_keys("La vida es una sola al final de la jornada")

try:
    multiSelect = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,
     "//label[contains(@id,'wsf-1-label-85-row-2')]")))
    multiSelect = driver.find_element(By.XPATH,"//label[contains(@id,'wsf-1-label-85-row-2')]")
    multiSelect.click()

except TimeoutException as ex:
    print(ex.msg)
    print("Do not found multiselect element")
    driver.close()

try:
    radio = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,
     "//label[contains(@for,'wsf-1-field-86-row-3')]")))
    radio = driver.find_element(By.XPATH,"//label[contains(@for,'wsf-1-field-86-row-3')]")
    radio.click()

except TimeoutException as ex:
    print(ex.msg)
    print("Do not found radio element")
    driver.close()

try:
    sistemoperator = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,
    "//select[@name='field_87[]']")))
    sistemo = Select(sistemoperator)
    sistemo.select_by_index(2)

except TimeoutException as ex:
    print(ex.msg)
    print("Do not found your sistem operator")
    driver.close()

try:
    optionSistem = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,
    "//select[contains(@id,'wsf-1-field-90')]")))
    optionS = Select(optionSistem)
    optionS.select_by_index(2)

except TimeoutException as ex:
    print(ex.msg)
    print("Do not found your sistem operator")
    driver.close()

events = driver.find_element(By.XPATH, "//input[@name='field_91']")
events.send_keys("2020/10/21")

calendar = driver.find_element(By.XPATH, "//input[@name='field_92']")
calendar.send_keys("2020/10/22")

try:
    upload = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
    "//input[contains(@id,'wsf-1-field-94')]")))
    upload = driver.find_element(By.XPATH,"//input[contains(@id,'wsf-1-field-94')]")
    upload.send_keys("/Users/adamslapaix/Downloads/name.png")
    time.sleep(2)

except TimeoutError as ex:
    inputForm = driver.find_element(By.XPATH, "//button[contains(@id,'wsf-1-field-93')]")    
    inputForm.click()
    print("Se envio el documento sin subir archivo")

inputForm = driver.find_element(By.XPATH, "//button[contains(@id,'wsf-1-field-93')]")   
driver.execute_script("arguments[0].scrollIntoView();", inputForm) 
time.sleep(3)
inputForm.click()
time.sleep(5)
driver.close()