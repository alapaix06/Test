from multiprocessing import set_forkserver_preload
# Importando framework de python para usar los unittest
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Se crea una clase donde testcaseIntegration representa el nombre de la clase, unittest llama el framework y el testcase indica que son testcases


class testcaseIntegration(unittest.TestCase):

    # def se usa para declarar funciones, donde setUp esta seteando los valores del navegador, self hace referencia a los elementos de la funcion
    def setUp(self):
        self.Navgdriver = webdriver.Chrome()

    # usar siempre test antes del nombre de la funcion
    def test_search(self):
        # aqui llamamos el valof la funcion del setUp y decimos que esa variables es igual a la del nav
        Navgdriver = self.Navgdriver

        Navgdriver.get('https://www.google.com')

        # el asserIn quiere decir los valores que va a buscar, luego le indicamos que valores buscara este dentro del navegador y luego indicamos donde lo buscara
        self.assertIn("Google", Navgdriver.title)

        searchBy = Navgdriver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        searchBy.send_keys("Hola Word")

        searchBy.send_keys(Keys.ENTER)

        time.sleep(3)

        # luego que pasara si no encuentra el assert, no in significa no esta en el navegador y page
        assert "No found element:" not in Navgdriver.page_source
    
    # el tearDown es para cerrar la sesion
    def tearDown(self):

        self.Navgdriver.close()

# el if hace referencia al modulo y este sera el codigo para que ejecute el script, el unittest.main va directo a la clase y empieza ejecutar.
if __name__ == '__main__':
    unittest.main()
