from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pythonping import ping
import requests
import subprocess
import time
browser = webdriver.Chrome(executable_path = 'bin\chromedriver.exe')
browser.get('http://192.168.1.1')
username=browser.find_element_by_id('username')
password=browser.find_element_by_id('psd')
capcha=browser.find_element_by_id('check_code')
capcha_verifier=browser.find_element_by_id('verification_code')
capcha_code=capcha.get_attribute('value')
username.send_keys('admin')
password.send_keys("messb0i5trange")
capcha_verifier.send_keys(capcha_code)
capcha_verifier.send_keys(Keys.RETURN)







