from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(
    executable_path=r'/Users/adamslapaix/Documents/drivers/chromedriver')

driver.maximize_window()
driver.get('https://demoqa.com/text-box')
time.sleep(1)

nombre = driver.find_element_by_xpath(
    "//input[@placeholder='Full Name' and @type='text']")
nombre.send_keys("Adams")

email = driver.find_element_by_xpath(
    "//input[@id='userEmail' and @placeholder='name@example.com']")
email.send_keys("adamslapaix.castillo@gmail.com")

address = driver.find_element_by_xpath("//textarea[@id='currentAddress' and @placeholder='Current Address']")
address.send_keys("Calle primera, Casa numero 12, esquina mar uno")
time.sleep(1)

permanentAddress = driver.find_element_by_xpath("//textarea[contains(@id, 'permanentAddress')]")
permanentAddress.send_keys("Calle Segunda")

# el excute_script siver para que selenium use un funcion de javascript
# el window.scrollTo sirve para hacer scroll y el () estaran las cordenadas x and y, siempre que no 
# usemos una debemos decir que es igual a 0

driver.execute_script("window.scrollTo(0,400)")

btn = driver.find_element_by_xpath("//button[@id='submit']").click()

driver.close()
