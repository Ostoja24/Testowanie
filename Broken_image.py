from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class broken_image:
    def __init__(self):
        pass
    #Page Elements
    page_title = "h3"
    img = ".img"

    def return_page_title(self, driver):
        element = WebDriverWait(driver, 7).until(ec.visibility_of_element_located((By.CSS_SELECTOR, self.page_title)))
        return element.text
    def return_images(self, driver):
        element = WebDriverWait(driver, 7).until(ec.visibility_of_element_located((By.CSS_SELECTOR, self.img)))
        element_write = element.screenshot_as_png()
        element_write()
