from doctest import DebugRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import unittest

class preRegister(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.debug = DebugRunner()
    
    def test_firstTest(self):
        driver = self.driver
        driver.get('https://www.educacionit.com/cursos-de-testing-qa')
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@id='area-course-intro-btn-courses']").click()
        repository = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'base-search-bar')]")))
        repository.send_keys("Hola")
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()

