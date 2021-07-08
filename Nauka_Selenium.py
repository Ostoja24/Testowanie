from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Edge(executable_path='C:/Users/tomcz/Documents/msedgedriver.exe')

driver.get('https://www.amazon.pl/')
search = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
search.send_keys('Python', Keys.ENTER)
search_confirmation = driver.find_element_by_css_selector(".a-color-state.a-text-bold")
assert search_confirmation.text == '"Python"'
driver.quit()