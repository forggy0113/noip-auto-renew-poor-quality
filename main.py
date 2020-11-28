from selenium import webdriver
import time
import psutil

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

username = ('xyz123@xxx.com') #輸入帳號
password = ('password') #輸入密碼

driver = webdriver.Chrome(options=options)
driver.get('https://my.noip.com/#!/dynamic-dns')

username_textbox = driver.find_element_by_name("username")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_name("Login")
login_button.submit()

Confirm_button =driver.find_element_by_css_selector('[class="btn btn-labeled btn-confirm"]')     

Confirm_button.click()

driver.quit()
