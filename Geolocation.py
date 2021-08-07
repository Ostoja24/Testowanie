from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class geo:
    #Page Elements
    button = "//*[@id='content']/div/button"
    latitude = "//*[@id='lat-value']"
    longitude = "//*[@id='long-value']"

    def links_click(self, driver):
        element = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, self.button)))
        element.click()

    def return_latitude_longitude_values(self, driver):
        element = WebDriverWait(driver, 7).until(ec.visibility_of_element_located((By.XPATH, self.latitude)))
        element1 = WebDriverWait(driver, 7).until(ec.visibility_of_element_located((By.XPATH, self.longitude)))
        return element.text, element1.text
