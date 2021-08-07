import time
import unittest
from pages.Geolocation import geo
from selenium import webdriver
from pathlib import Path
from selenium.webdriver import Chrome, ChromeOptions
from assertpy import soft_assertions, assert_that


class ChallengingDom(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        path_to_driver = Path("drivers/chromedriver.exe")
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--able-geolocation")
        driver = webdriver.Chrome(executable_path=path_to_driver, options=options)

    @classmethod
    def tearDownClass(cls) -> None:
        driver.quit()

    def test_01_geolocation_coordinates(self):
        gg = geo()
        driver.get("https://the-internet.herokuapp.com/geolocation")
        gg.links_click(driver)
        time.sleep(5)
        lat, long = gg.return_latitude_longitude_values(driver)
        with soft_assertions():
            assert_that(lat).is_equal_to("52.379648")
            assert_that(long).is_equal_to("16.95744")


if __name__ == '__main__':
    unittest.main()
