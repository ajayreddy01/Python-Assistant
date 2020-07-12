from requirements import *
global insta
def insta():
    import selenium
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    USERNAME=str(input("Enetr your user name:"))
    PASSWORD= str(input("Enter Your Password:"))

    chromedriver_path ='C:/chromedriver.exe'

    webdriver = webdriver.Chrome(executable_path=chromedriver_path)

    webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    sleep(5)

    username = webdriver.find_element_by_name('username')
    username.send_keys(USERNAME)
    password = webdriver.find_element_by_name('password')
    password.send_keys(PASSWORD)

    button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div')
    button_login.click()
    sleep(6)
    not_now  = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
    not_now.click()
    sleep(6)
    notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
    notnow.click()
    def inbox():
        button_inbox = webdriver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(2) > a > svg')
        button_inbox.click()
        sleep(10)
        button_home = webdriver.find_element_by_css_selector('#react-root > section > div > div._lz6s.Hz2lF > div > div.ctQZg > div > div:nth-child(1) > div > a > svg')
        button_home.click()
    inbox()
    sleep(10)
    def activity():
        button_activity = webdriver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(4) > a > svg')
        button_activity.click()
        sleep(2)
    activity()

    webdriver.quit()
