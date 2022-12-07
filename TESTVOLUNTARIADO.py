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

class TestTESTVOLUNTARIADO():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tESTVOLUNTARIADO(self):
    self.driver.get("https://www.rescatewildlife.org/")
    self.driver.set_window_size(1512, 847)
    element = self.driver.find_element(By.LINK_TEXT, "Volunteer")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Volunteer").click()
    element = self.driver.find_element(By.LINK_TEXT, "Volunteer")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "form-field-name").click()
    dropdown = self.driver.find_element(By.ID, "form-field-name")
    dropdown.find_element(By.XPATH, "//option[. = 'Local Volunteer']").click()
    self.driver.find_element(By.ID, "form-field-field_97f8baa").click()
    self.driver.find_element(By.ID, "form-field-field_97f8baa").send_keys("Sebastian")
    self.driver.find_element(By.ID, "form-field-field_07fc2d8").send_keys("Trejos Brenes")
    self.driver.find_element(By.ID, "form-field-field_70f27fc").send_keys("sebastrejos76@gmail.com")
    self.driver.find_element(By.ID, "form-field-field_29b088f").send_keys("84274646")
    self.driver.find_element(By.ID, "form-field-field_3740ed2").send_keys("Costa Rica")
    self.driver.find_element(By.ID, "form-field-field_8ca0f52").click()
    dropdown = self.driver.find_element(By.ID, "form-field-field_8ca0f52")
    dropdown.find_element(By.XPATH, "//option[. = 'Spanish']").click()
    self.driver.find_element(By.ID, "form-field-field_d4035f9").click()
    dropdown = self.driver.find_element(By.ID, "form-field-field_d4035f9")
    dropdown.find_element(By.XPATH, "//option[. = 'Web search']").click()
    self.driver.switch_to.frame(1)
    self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
    self.driver.switch_to.default_content()
    self.driver.find_element(By.CSS_SELECTOR, ".elementor-size-sm > span").click()
  
