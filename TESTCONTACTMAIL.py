# Importamos todas las librerias que nos requiere el uso de Selenium en Python
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTESTCONTACTMAIL():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tESTCONTACTMAIL(self):
    
    #El primer paso para testear el envio del mail es abrir la url de inicio
    self.driver.get("https://www.rescatewildlife.org/es/inicio/")
    #Accedemos con un click al "linkText=info@rescatewildlife.org" esto para enviar la solicitud o peticion deseada para el caso
    self.driver.set_window_size(1512, 847) 
    self.driver.find_element(By.LINK_TEXT, "info@rescatewildlife.org").click()
