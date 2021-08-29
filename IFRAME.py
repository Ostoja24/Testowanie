from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class iframe:
    #Page elements
    frame = "//*[@id='content']/div/ul/li[2]/a"
    text_box = "mce_0_ifr"
    bold_button = "//button[@title='Bold']"
    italic_button = "//button[@title='Italic']"
    left_align = "//button[@title='Align left']"
    middle_align = "//button[@title='Align center']"
    right_align = "//button[@title='Align right']"
    justify = "//button[@title='Justify']"
    format_button = "div[role='menubar'] button:nth-child(4)"
    bold2_button = "//div[text()='Bold']"

    def iframe_click(self, driver):
        i_frame= WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, self.frame)))
        i_frame.click()

    def text_box_click(self,driver):
        tb = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.ID, self.text_box)))
        tb.click()
    def bold_button_click(self,driver):
        bb = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, self.bold_button)))
        bb.click()
    def italic_button_click(self, driver):
        ib = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, self.italic_button)))
        ib.click()
    def left_align_click(self, driver):
        la = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, self.left_align)))
        la.click()
    def middle_align_click(self, driver):
        ma = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, self.middle_align)))
        ma.click()
    def right_align_click(self, driver):
        ra = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, self.right_align)))
        ra.click()
    def justify_click(self, driver):
        jc = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, self.justify)))
        jc.click()
    def format_button_click(self, driver):
        fb = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.format_button)))
        fb.click()
    def bold2_button_click(self, driver):
        bb2 = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.XPATH, self.bold2_button)))
        bb2.click()