from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('./chromedriver.exe')
browser.implicitly_wait(10)


def test_SearchEmptyForm():
    browser.get('http://6e6057dcc96e.ngrok.io/jobseeker/auth/')

    # login
    email = browser.find_element_by_id("jobseeker-signin-email-input")
    email.send_keys('a@a.com')

    password = browser.find_element_by_id('jobseeker-signin-password-input')
    password.send_keys('123456')

    login_btn = browser.find_element_by_class_name('button')
    login_btn.click()

    search_bar = browser.find_element_by_id('job-search-input')
    search_bar.clear()

    search_button = browser.find_elements_by_class_name('button')
    search_button.button()

    validation_message = search_bar.get_attribute("validationMessage")
    if validation_message != '':
        print('success')
    else:
        print('failed')


test_SearchEmptyForm()
