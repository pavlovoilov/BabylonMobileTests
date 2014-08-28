import os
import unittest
from appium import webdriver
import allure
from settings import *

class BaseTest(unittest.TestCase):

    @allure.step('Set up')
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = PLATFORM_NAME
        desired_caps['platformVersion'] = PLATFORM_VERSION
        desired_caps['deviceName'] = DEVICE_NAME

        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),APP_PATH))
        desired_caps['appPackage'] = APP_PACKAGE
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @allure.step('Tear down')
    def tearDown(self):
        self.driver.quit()
