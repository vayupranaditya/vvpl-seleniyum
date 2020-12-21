from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('./chromedriver.exe')
browser.implicitly_wait(10)


def test_SearchEmptyForm():
    browser.get('http://f94c1a433001.ngrok.io/jobseeker/auth/')

    # login
    email = browser.find_element_by_id("jobseeker-signin-email-input")
    email.send_keys('inibukanemail')

    password = browser.find_element_by_id('jobseeker-signin-password-input')
    password.send_keys('123456')

    login_btn = browser.find_element_by_class_name('button')
    login_btn.click()

    validation_message = email.get_attribute("validationMessage")
    if validation_message != '':
        print('success', validation_message)
    else:
        print('failed')


test_SearchEmptyForm()
