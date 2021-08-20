import unittest
from selenium import webdriver
# Sirve como exception cuando para cuando queramos validar la presencia de un elemento
from selenium.common.exceptions import NoSuchElementException
# Ayuda a llamar las excepciones que queremos validar
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    # Identifica si el elemento esta presente
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    def tearDown(self):
        self.driver.quit()

    # permite encontra los elementos
    # how = tipo de elector
    # what = valor que tiene
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True
