from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
driver = webdriver.Chrome(executable_path=r'/Users/adamslapaix/Documents/drivers/chromedriver')
driver.get("http://www.python.org")

print ("Page title is: " + driver.title)

driver.close()


navDriver = webdriver.Firefox(executable_path=r'/Users/adamslapaix/Documents/drivers/geckodriver')
navDriver.get("http://www.python.org")

print ("Page title is: " + navDriver.title)
navDriver.close()