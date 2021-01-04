# coding=u\
#  tf-8
"""
==========================
author:Xu
time:2020/12/24 
==========================
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

"""
优先级：
1.优先使用id
2.次选name
3.css
4.xpath
"""