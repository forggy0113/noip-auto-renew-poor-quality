from selenium import webdriver
import time
import psutil
import json
from os import _exit

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

with open("config.json" , "r" , encoding="utf-8") as jfile:
    jdata = json.load(jfile)

username = (jdata["username"]) #輸入帳號   #在json裡面打
password = (jdata["password"]) #輸入密碼   #同上

driver = webdriver.Chrome(options=options,executable_path=jdata["PATH"])    #PATH可以在json裡面改
driver.get('https://my.noip.com/#!/dynamic-dns')

username_textbox = driver.find_element_by_name("username")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_name("Login")
login_button.submit()


n = 0
while n <= 3:
    try:
        driver.find_element_by_css_selector('[class="btn btn-labeled btn-confirm"]')
    except:
        driver.quit()
        _exit(0)

    Confirm_button =driver.find_element_by_css_selector('[class="btn btn-labeled btn-confirm"]')     
    Confirm_button.click()
    n += 1