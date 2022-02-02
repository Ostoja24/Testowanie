# Table of contents
# [General info]
Repo has several test files in Python. The main aim is to present different testcases in Python using sites for testing education. 
# [Technologies]
In testcases are used technologies/modules like below:
* Python 3.9
* Pytest
* Selenium Webdriver
* Unittest
* Chrome
* Microsoft Edge
# [Setup]
At the beginning, you can install IDE with Python (like Pycharm) and create a virtual environment (venv). Next, you should activate it. It's crucial to install in your IDE presented modules to launch testcases properly:
```
$ pip install selenium
$ pip install msedge-selenium-tools selenium==3.141 or pip install selenium-tools
$ pip install assertpy
```
For a setting driver, it needs appriopriate path to driver. For example in commands like: driver = webdriver.Chrome("here put the driver path")
# [Features]
* Dropdown.py - Testcase for visible elements in https://rejkowicz.pl/blog/lista-rozwijana-html5/ page
* Geolocation.py - Testcase in which geocoordinates are tested for right values 
* Test_00_visit_demo.py - Testcase for assertion elements in https://www.demoqa.com/ page
* Test_01_broken_images.py - Testcase for testing page title and downloading image from https://the-internet.herokuapp.com/broken_images
* Test_03_auth.py - Testcase for authorization module testing, visibility elements, windows creation, screenshot making in https://the-internet.herokuapp.com/
* Test_04_Geolocation (1).py - Testcase for geolocation in https://the-internet.herokuapp.com/geolocation
* Test_06_iFRAME.py - Testcase for movements in iFrame form in https://the-internet.herokuapp.com/frames
* Test_11_Key_page.py - Testcase for keys page and clicking them in https://the-internet.herokuapp.com/key_presses
