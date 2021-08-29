import unittest
from pages.Keys import key_page
from selenium import webdriver
from pathlib import Path
from selenium.webdriver import Chrome, ChromeOptions


class keysite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        path_to_driver = Path("C:\TestFiles\chromedriver.exe")
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(executable_path=path_to_driver, options=options)

    @classmethod
    def tearDownClass(cls) -> None:
        driver.quit()

    def test11_keysitetest(self):
        kp = key_page()
        driver.get("https://the-internet.herokuapp.com/key_presses")
        kp.key_page_backspace(driver)
        self.assertEqual(kp.key_result_visible(driver),"You entered: BACK_SPACE")
        kp.key_page_down(driver)
        self.assertEqual(kp.key_result_visible(driver), "You entered: DOWN")
        kp.key_page_up(driver)
        self.assertEqual(kp.key_result_visible(driver), "You entered: UP")
        kp.key_page_g(driver)
        self.assertEqual(kp.key_result_visible(driver), "You entered: G")