import time
import unittest
from selenium import webdriver
from pathlib import Path
from msedge.selenium_tools import Edge
from msedge.selenium_tools import EdgeOptions
from selenium.webdriver import ActionChains


class ThirdTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        global driver
        path_to_driver = Path("C:/TestFiles/msedgedriver.exe")
        options = EdgeOptions()
        options.use_chromium = True
        options.add_argument("--start-maximized")
        driver = Edge(executable_path=path_to_driver)

    @classmethod
    def tearDownClass(cls) -> None:
        driver.quit()

    def test_03_auth(self):
        username = "admin"
        password = "admin"
        driver.get("https://"+username+":"+password+"@the-internet.herokuapp.com/basic_auth")
        time.sleep(3)
        text_1 = driver.find_element_by_css_selector("div[class='example'] p").text
        assert "Congratulations!" in text_1
    def test_04_auth(self):
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        driver.get_screenshot_as_file("C:\\TestFiles\\zrzut_ekranu.png")
    def test_06_auth(self):
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_xpath("//a[normalize-space()='Floating Menu']").click()
        floating_menu = driver.find_element_by_xpath('//li')
        driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
        time.sleep(3)
        if floating_menu.is_displayed():
            print ('Element jest na stronie')
        else:
            print ('Element nie jest na stronie')
    def test07_auth(self):
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_xpath("//a[normalize-space()='Multiple Windows']").click()
        driver.find_element_by_xpath("//*[@id='content']/div/a").click()
        time.sleep(3)
        if len(driver.window_handles) == 2:
            print("Tworzy prawidłowo okno")
        else:
            print("Nie tworzy okna")


class test_right:
    def test_05_auth(self):
        driver.get("https://the-internet.herokuapp.com/context_menu")
        element1 = driver.find_element_by_xpath("//div[@id='hot-spot']")
        actionChains = ActionChains(driver)
        actionChains.context_click(element1).perform()
        time.sleep(3)
        popup1 = driver.switch_to.alert
        assert "You selected a context menu" in popup1.text
ThirdTest.setUpClass()
test_click_right = test_right()
test_click_right.test_05_auth()
ThirdTest.tearDownClass()

if __name__ == '__main__':
    unittest.main()