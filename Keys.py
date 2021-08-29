from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

class key_page:
    #elements
    key_box = ("//input[@id='target']")
    key_result = ("#result")

    def key_page_click(self, driver):
        key_element = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, self.key_box)))
        key_element.click()
    def key_result_visible(self, driver):
        key_result_element = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.key_result)))
        return key_result_element.text
    def key_page_backspace(self, driver):
        key_enter = WebDriverWait(driver, 7).until(ec.visibility_of_element_located((By.XPATH, self.key_box)))
        key_enter.send_keys(Keys.BACKSPACE)
    def key_page_down(self, driver):
        key_down = WebDriverWait(driver, 7).until(ec.visibility_of_element_located((By.XPATH, self.key_box)))
        key_down.send_keys(Keys.DOWN)
    def key_page_up(self, driver):
        key_up = WebDriverWait(driver, 7).until(ec.visibility_of_element_located((By.XPATH, self.key_box)))
        key_up.send_keys(Keys.UP)
    def key_page_g(self, driver):
        key_g = WebDriverWait(driver, 7).until(ec.visibility_of_element_located((By.XPATH, self.key_box)))
        key_g.send_keys("G")
