from time import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class preRegister(unittest.TestCase):
    def setUp(self):
        self.navDriver = webdriver.Chrome()

    def test_completePreregister(self):

        navDriver = self.navDriver

        navDriver.get(
            'https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

        insertEmail = navDriver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]')
        insertEmail.send_keys('adamslapaix.castillo@gmail.com')
        insertEmail.send_keys(Keys.RETURN)

        insertPass = navDriver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/input')
        insertPass.send_keys('Lpxbroth06')
        insertPass.send_keys(Keys.RETURN)
        time.sleep(1.5)

        insertArticle = navDriver.find_element_by_xpath(
            '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div[1]/input')
        insertArticle.send_keys('Apple Watch')
        insertArticle.send_keys(Keys.RETURN)

        self.assertIn('Succesfull', navDriver.title)

        assert "Not found key in:" not in navDriver.page_source

    def test_completeRegister(self):
        navDriver = self.navDriver
        navDriver.get('https://www.google.com')

    def tearDown(self):
        self.navDriver.close()


if __name__ == '__main__':
    preRegister(unittest.main())
