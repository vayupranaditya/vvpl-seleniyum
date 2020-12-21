from selenium import webdriver
import unittest
import time

DRIVER_LOCATION = '/usr/bin/chromedriver'
JOBSEEKR_URL = 'http://localhost:8001/'
TEST_CASES = [
    {
        'email': 'a@a.com',
        'password': '',
        'types': ['password'],
        'msg': 'Failed to assert that password is required'
    },
    {
        'email': '',
        'password': '123456',
        'types': ['email'],
        'msg': 'Failed to assert that email is required'
    },
    {
        'email': '',
        'password': '',
        'types': ['email', 'password'],
        'msg': 'Failed to assert that email and password is required'
    },
]


class TestLogin(unittest.TestCase):
    def login(self, email, password):
        login_form = browser.find_elements_by_tag_name('form')[0]
        email_input, pwd_input = login_form.find_elements_by_tag_name('input')[1:3]
        email_input.send_keys(email)
        pwd_input.send_keys(password)

        login_btn = login_form.find_elements_by_tag_name('button')[0]
        login_btn.click()

        return login_form

    def run_test_case(self, test_case):
        login_form = self.login(test_case['email'], test_case['password'])
        invalids = login_form.find_elements_by_css_selector('input:invalid')
        actual_types = [invalid.get_attribute('type') for invalid in invalids]
        self.assertTrue(
            len(invalids) == len(test_case['types']) and actual_types == test_case['types'],
            test_case['msg']
        )
        browser.refresh()


    def test_required_entries_filled(self):
        for test_case in TEST_CASES:
            self.run_test_case(test_case)

    @classmethod
    def tearDownClass(cls):
        browser.quit()


if __name__ == '__main__':
    browser = webdriver.Chrome(DRIVER_LOCATION)
    browser.get(JOBSEEKR_URL)
    jobseeker_auth_btn = browser.find_elements_by_tag_name('a')[0]
    jobseeker_auth_btn.click()
    time.sleep(1)

    unittest.main()
