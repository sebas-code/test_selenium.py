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

class TestTESTDONAR():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_tESTDONAR(self):
    
    self.driver.get("https://www.rescatewildlife.org/")
    
    self.driver.set_window_size(1512, 847)
    
    self.vars["window_handles"] = self.driver.window_handles
    
    self.driver.find_element(By.LINK_TEXT, "Via Paypal").click()
    
    self.vars["win405"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win405"])
    self.driver.find_element(By.ID, "currencyAmount").click()
  
