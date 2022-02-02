import unittest
from pathlib import Path
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions

from pages.home_page import HomePage


class Test_00(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        global driver
        path_to_driver = Path("C:\TestFiles\msedgedriver.exe")
        options = EdgeOptions()
        options.use_chromium = True
        options.add_argument("--start-maximized")
        driver = Edge(executable_path=path_to_driver)

    @classmethod
    def tearDownClass(cls) -> None:
        driver.quit()

    def test_00_visit_demoqa_website(self):
        driver.get("https://www.demoqa.com/")
        footer_text = driver.find_element_by_css_selector("footer span").text
        assert footer_text == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."

    def test_01_verify_elements_on_website(self):
        elements = driver.find_elements_by_css_selector(".card-body h5")
        list_of_elements_names = ["Elements", "Forms", "Alerts, Frame & Windows", "Widgets", "Interactions", "Book Store Application"]
        for _ in range(len(list_of_elements_names)):
            assert elements[_].text == list_of_elements_names[_]


    def test_02_click_on_elements_widget(self):
        hp = HomePage()
        hp.click_on_elements_widget(driver)
        input()


if __name__ == '__main__':
    unittest.main()
