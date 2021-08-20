import unittest

from selenium import webdriver

class SearchTests(unittest.TestCase):
    

    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=r"./chromedriver/chromedriver.exe")
        driver = cls.driver
        driver.get("http://demo.onestepcheckout.com/")
        # maximiza la pantalla para evitar errores con estilos css
        driver.maximize_window()
        # añade una pausa
        driver.implicitly_wait(15)


    def test_search_tee(self):
        driver = self.driver    
        search_field = driver.find_element_by_name('q')
        # limpia campo de busqueda en caso de que exista un texto
        search_field.clear()
        # simula la escritura de un teclado
        search_field.send_keys('tee')
        # muestra los resultados
        search_field.submit()


    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))


#    def test_search_text_field(self):
#        # campo de busqueda, en este caso a travez del id
#        search_field = self.driver.find_element_by_id("search")

    
#    def test_search_text_field_by_name(self):
#        search_field = self.driver.find_element_by_name("q")


#    def test_search_text_field_by_class_name(self):
#        search_field = self.driver.find_element_by_class_name("input-text")


#    def test_search_button_ennabled(self): 
        # identifica si un boton esta disponible
#        button = self.driver.find_element_by_class_name("button")

    #Metodo para contar cuantas imagenes hay de promocion en el banner
#    def test_count_of_promo_banner_images(self):
#        banner_list = self.driver.find_element_by_class_name("promos")
        # almacena la busqueda de los banners
#        banners = banner_list.find_elements_by_tag_name('img')
        # validacion que verifica si la condicion se cumple o no
#        self.assertEqual(3, len(banners))

    # Metodo que permite identificar objectos cuando no es directamente explicito
#    def test_vip_promo(self):
        # muestra donde se encuntra los nodos de la imagen a atravez de XML
#        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')


#    def test_shopping_cart(self):
#        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")


    def tearDown(cls):
        cls.driver.quit()



if __name__ == "__main__":
    unittest.main(verbosity= 2)
