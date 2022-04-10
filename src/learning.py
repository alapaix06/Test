from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


navegador = webdriver.Chrome()

navegador.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
time.sleep(0.8)

ingreasrcorreo = navegador.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]')
ingreasrcorreo.send_keys('adamslapaix.castillo@gmail.com')
ingreasrcorreo.send_keys(Keys.ENTER)

ingresaclave = navegador.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/input')
ingresaclave.send_keys('Lpxbroth06')
ingresaclave.send_keys(Keys.ENTER)
time.sleep(5)
navegador.close()
