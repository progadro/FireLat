from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pythonping import ping
import requests
import subprocess
import os
import time
properties = Options()
properties.headless = True
properties.binary_location=r'bin\chromium\chrome.exe'
browser = webdriver.Chrome(executable_path='bin\chromedriver.exe',options=properties)
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
browser.switch_to.frame('topFrame')
browser.execute_script("on_catolog('1')")
browser.execute_script("on_menu('1')")
browser.switch_to.parent_frame()
browser.switch_to.frame('mainFrame')
time.sleep(2)
browser.execute_script("on_submit('sv')")
time.sleep(4)
browser.switch_to.parent_frame()
browser.switch_to.frame('topFrame')
logout=browser.find_element_by_xpath(r'/html/body/form/table[2]/tbody/tr[1]/td[2]/font[2]/input')
logout.click()
browser.close()
os.system("taskkill /f /im chromedriver.exe")
os.system("taskkill /f /im chrome.exe")

















