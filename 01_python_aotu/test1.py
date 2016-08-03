import urllib

html = urllib.urlopen('https://www.baidu.com/').info()

print html
