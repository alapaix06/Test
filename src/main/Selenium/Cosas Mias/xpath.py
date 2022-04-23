import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class  xpath(unittest.TestCase):
    def setUp(self):
        self.navDriver = webdriver.Chrome() #executable_path=r"C:\Users\adams\Desktop\chromedriver.exe")
    
    def test_xpath(self):
        navDriver = self.navDriver
        timeWait = 3
        navDriver.get('https://www.google.com')
        time.sleep(timeWait)
        insertSearch =navDriver.find_element_by_xpath('//*[@name=‘q’]')
        insertSearch.send_keys('Google', Keys.RETURN)
        time.sleep(timeWait)


if __name__ == '__main__':
    xpath(unittest.main())