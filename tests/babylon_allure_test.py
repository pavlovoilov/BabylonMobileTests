from time import sleep
import allure

from BaseTest import BaseTest

class AllureTests(BaseTest):

    @allure.step('Test case #1')
    def test_successful_login(self):
        self.driver.find_element_by_id('com.babylon:id/sign_in_text_view').click();
        self.driver.find_element_by_id('com.babylon:id/emailEdt').send_keys('vici.edisson@gmail.com')
        self.driver.find_element_by_id('com.babylon:id/passwordEdt').send_keys('password')
        self.driver.find_element_by_id('com.babylon:id/signInBtn').click()
        try:
            self.driver.hide_keyboard()
        except:
            pass
        sleep(3)
        assert (1, 1)

    @allure.step('Test case #2')
    def test_powering(self, input=2, expected=4):
        self.assertEqual(input**2, expected)

