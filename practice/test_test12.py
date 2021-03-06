# Generated by Selenium IDE
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

class TestTest12():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_test12(self):
    self.driver.get("https://www.baidu.com/")
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.LINK_TEXT, "更多").click()
    self.vars["win4494"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win4494"])
    self.driver.find_element(By.ID, "kw").click()
    self.driver.find_element(By.ID, "kw").send_keys("百科")
    self.driver.find_element(By.ID, "su").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.XPATH, "//div[@id=\'1\']/h3/a/em[2]").click()
    self.vars["win9383"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win9383"])
  
