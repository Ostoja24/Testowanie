import unittest
from pages.Broken_image import broken_image
from selenium import webdriver
from pathlib import Path
from selenium.webdriver import Edge
from msedge.selenium_tools import Edge
from msedge.selenium_tools import EdgeOptions


class broken_images (unittest.TestCase):
    @classmethod
    def setUpClass(self):
        global driver
        path_to_driver = Path("C:\TestFiles\msedgedriver.exe")
        options = EdgeOptions()
        options.use_chromium = True
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(executable_path = path_to_driver)

    @classmethod
    def tearDown(self) -> None:
        driver.quit()

    def test_01_navigate_to_page_title(self):
        bi = broken_image()
        driver.get("https://the-internet.herokuapp.com/broken_images")
        element_title = bi.return_page_title(driver)
        print(element_title)
        self.assertEquals(element_title, 'Broken Images')
    def test_02_show_images(self):
        bi = broken_image()
        driver.get("https://the-internet.herokuapp.com/broken_images")
        element = bi.return_images(driver)
        element()


if __name__ == '__main__':
    unittest.main()
