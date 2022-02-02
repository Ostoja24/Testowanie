from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
class testing_dropdown(self):
  def test_dropdown(self):
driver = webdriver.Chrome("C:\TestFiles\chromedriver.exe")

driver.maximize_window()
actions = ActionChains(driver)
driver.get('https://rejkowicz.pl/blog/lista-rozwijana-html5/')
element = driver.find_element_by_xpath("//p[10]//select[1]")
actions.move_to_element(element).click().perform()
drp = Select(element)

drp.select_by_visible_text("Pierwsza opcja")
time.sleep(2)
drp.select_by_index(1)
time.sleep(2)
drp.select_by_value("4")
time.sleep(2)

driver.quit()
