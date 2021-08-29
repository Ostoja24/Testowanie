import unittest
from pathlib import Path
from pages.IFRAME import iframe
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions


class clicker (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # global driver
        path_to_driver = Path("C:\TestFiles\chromedriver.exe")
        options = ChromeOptions()
        # options.add_argument("--headless")
        cls.driver = Chrome(executable_path = path_to_driver, options=options)

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()

    def test_06_iframe(self):
        self.driver.get("https://the-internet.herokuapp.com/frames")
        frame1= iframe()
        frame1.iframe_click(self.driver)
        text_box = self.driver.find_element_by_id(iframe.text_box)
        text_box.send_keys(Keys.CONTROL + "a")
        text_box.send_keys(Keys.DELETE)
        text_box.send_keys("Test udany")
        text_box.send_keys(Keys.CONTROL + "a")
        frame1.bold_button_click(self.driver)
        frame1.italic_button_click(self.driver)
        frame1.left_align_click(self.driver)
        frame1.middle_align_click(self.driver)
        frame1.right_align_click(self.driver)
        frame1.justify_click(self.driver)
        frame1.format_button_click(self.driver)
        frame1.bold2_button_click(self.driver)


