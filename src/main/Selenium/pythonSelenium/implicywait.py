from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r'/Users/adamslapaix/Documents/drivers/chromedriver')
driver.get('https://demoqa.com/text-box')
driver.maximize_window()

# El implicitly wait sirve para que la pagina se tome un tiempo si no exuentra algun elemento, si la pagina encuentra el elemento, esta correra de manera normal y lo ignorara.
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("Adams")
time.sleep(5)


driver.get('https://www.google.com')

driver.execute_script("window.history.go(-1)")
time.sleep(1)

driver.close()
