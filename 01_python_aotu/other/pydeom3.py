# coding = utf-8
from selenium import webdriver
import time

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("wfm")
browser.find_element_by_id("su").click()
time.sleep(10)
browser.quit()