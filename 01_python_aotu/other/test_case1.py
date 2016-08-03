# coding=utf-8
from pyse import Pyse, TestRunner
from time import sleep


def test_baidu():
    ''' baidu search key : pyse '''
    driver = Pyse("chrome")
    driver.open("http://10.1.0.50/middlecas/login?service=http://10.1.0.52:8080/middleresource/shiro-cas")
    # driver.type("id=>kw","pyse")
    # driver.click("css=>#su")
    sleep(1)
    assert "pyse" in driver.get_title()
    driver.quit()

if __name__ == '__main__':
    test_pro = TestRunner()
    test_pro.run()
