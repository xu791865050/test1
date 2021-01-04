"""
==========================
-*- coding: utf-8 -*-
@file   :basepage.py 
author  :Xu
@Email  :1009620783
time    :2020/12/26 
==========================
"""
# from Common import logger
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from selenium.webdriver.common.by import By
import datetime
import time
from selenium import webdriver

class Basepage:

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
    # 等待元素可见
    def wait_elevisible(self, locator, doc="",times=30, poll_frequency=0.5):
        logging.info("等待元素可见》》{}".format(locator))
        try:
            # 开始等待时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, locator, times,poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待时间
            end = datetime.datetime.now()
            logging.info("开始等待时间点：{}，结束等待时间点：{}，等待时长为：{}".
                         format(start, end, end - start))
        except:
            logging.exception("等待元素失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 等待元素存在
    def wait_elevisible1(self,locator, msg_doc="" ):
        logging.info("等待元素存在》》{}".format(locator))
        try:
            self.wait_elevisible(locator,msg_doc)
            return True
        except:
            return False
    # 文件上传非input
    def not_input(self, text,msg_doc="" ):
        logging.info("文件上传非input》》{}".format(text))
        try:
            pyk = PyKeyboard()
            pyk.tap_key(pyk.shift_key)
            time.sleep(1)
            pyk.type_string(text)
            time.sleep(1)
            pyk.tap_key(pyk.enter_key)
        except:
            logging.info("文件上传非input》》失败")
            self.save_screenshot(msg_doc)
            raise






        # 查找
    def get_element(self, locator, doc=""):
        logging.info("查找元素可见》》{}".format(locator))
        try:
            self.wait_elevisible(locator, doc=doc)
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=""):
        # 查找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        logging.info("{0}》点击元素{1}".format(doc, locator))
        try:
            ele.click()
        except:
            logging.exception("元素点击操作失败！！！")
            self.save_screenshot(doc)
            raise

    # 文本输入操作
    def input_text(self, locator, text, msg_doc=""):
        ele = self.get_element(locator, msg_doc)
        try:
            ele.send_keys(text)
        except:
            logging.exception("元素输入失败！！！")
            self.save_screenshot(msg_doc)
            raise

    #  获取元素的文本内容
    def get_text(self, locator, msg_doc=""):
        ele = self.get_element(locator, msg_doc)
        try:
            return ele.text
        except:
            logging.exception("获取元素文本失败！！！")
            self.save_screenshot(msg_doc)
            raise

    # 查找元素的属性
    def get_elment_attribute(self,locator,attr, msg_doc=""):
        ele = self.get_element(locator, msg_doc)
        try:
            return ele.get_attribute(attr)
        except:
            logging.exception("获取元素属性失败！！！")
            self.save_screenshot(msg_doc)
            raise


    # 截图
    def save_screenshot(self, name):
        # 图片名称：模块名称+页面名称+操作名称+时间.png
        file_name = "截屏路径"+"{}_{}".format(name,time)
        self.driver.save_screenshot(file_name)
        logging.info("截取网页陈宫。文件路径为：{}".format(file_name))