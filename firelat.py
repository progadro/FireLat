from pythonping import ping
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import os
import logging
import subprocess
import time
response_list=ping('155.133.232.98')
print("==FireLat v1.0== \nUtility to fix BSNL Routing issues.\nCoded by Strange.")
lat=response_list.rtt_avg_ms
print("Latency before run-time= ",lat,"ms")
print("IP before run-time: ",requests.get("http://ipconfig.in/ip").text)
login = 0
properties = Options()
properties.headless = True
properties.binary_location = r'bin\chromium\chrome.exe'
kill_driver = 0
browser = webdriver.Chrome(executable_path='bin\chromedriver.exe', options=properties)
browser.get('http://192.168.1.1')
username = browser.find_element_by_id('username')
password = browser.find_element_by_id('psd')
capcha = browser.find_element_by_id('check_code')
capcha_verifier = browser.find_element_by_id('verification_code')
capcha_code = capcha.get_attribute('value')
username.send_keys('admin')
password.send_keys("messb0i5trange")
capcha_verifier.send_keys(capcha_code)
capcha_verifier.send_keys(Keys.RETURN)
###############################
# Checking Latency
###############################
while lat > 45:
    print("Restarting Modem..")
    browser.switch_to.parent_frame()
    browser.switch_to.frame('topFrame')
    browser.execute_script("on_catolog('1')")
    browser.execute_script("on_menu('1')")
    browser.switch_to.parent_frame()
    time.sleep(2)
    browser.switch_to.frame('mainFrame')
    time.sleep(2)
    browser.execute_script("on_submit('sv')")
    time.sleep(8)
    print("Restart Complete.")
    response_list = ping('155.133.232.98')
    lat = response_list.rtt_avg_ms
    print("Latency after restart= ", lat, "ms")
    print("IP address after restart: ", requests.get("http://ipconfig.in/ip").text)
    if lat < 45:
        kill_driver = 1
        browser.switch_to.parent_frame()
        browser.switch_to.frame('topFrame')
        logout = browser.find_element_by_xpath(r'/html/body/form/table[2]/tbody/tr[1]/td[2]/font[2]/input')
        logout.click()
        browser.close()
        os.system("taskkill /f /im chromedriver.exe")
        os.system("taskkill /f /im chrome.exe")
        break
print("==Process Complete==")
print("Final latency= ",lat,"ms")
print("IP address: ", requests.get("http://ipconfig.in/ip").text)
input("Press Enter to Quit.")