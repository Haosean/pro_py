
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep

# http://10.1.0.54/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=ad53d86d-24d5-40fc-99c7-3a799983aa00&isZhu=1&classroomId=3b56d0d6-bae4-4e42-b0f7-0534fcbd64c9&interactType=false&created=0&mcuIds=ee8e08a4-7113-404d-ab63-e938ce14c631
# http://10.1.0.54/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=2ef96704-b305-4991-a1c2-b69111a1834e&isZhu=1&classroomId=7a562357-4a68-40b4-bb30-50c7da90512e&interactType=false&created=0&mcuIds=ee8e08a4-7113-404d-ab63-e938ce14c631
# http://10.1.0.54/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=838ff881-e1f3-4515-96c2-7e405c1bbc7c&isZhu=1&classroomId=7a562357-4a68-40b4-bb30-50c7da90512e&interactType=false&created=0&mcuIds=ee8e08a4-7113-404d-ab63-e938ce14c631


def login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = "http://10.1.0.54"
    verificationErrors = []
    accept_next_alert = True
    driver.get(base_url + "/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=2ef96704-b305-4991-a1c2-b69111a1834e&isZhu=1&classroomId=7a562357-4a68-40b4-bb30-50c7da90512e&interactType=false&created=0&mcuIds=ee8e08a4-7113-404d-ab63-e938ce14c631")
    Select(driver.find_element_by_id("platform")).select_by_visible_text(
        u"河南教育局")
    driver.find_element_by_id("s_username").clear()
    driver.find_element_by_id("s_username").send_keys("hnsadmin")
    driver.find_element_by_id("s_password").clear()
    driver.find_element_by_id("s_password").send_keys("111111")
    # 登录
    driver.find_element_by_name("submit").click()
    driver.maximize_window()
    sleep(10)
    # 开课
    driver.find_element_by_id("pc_startButton").click()

    sleep(300)
    # 开课
    driver.find_element_by_id("pc_startButton").click()

    driver.maximize_window()
    sleep(2)
    sleep(10)


if __name__ == '__main__':
    login()
