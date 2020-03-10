import os
import sys
os.getcwd()#返回当前进程的工作目录
sys.path.append(os.getcwd())#将模块路径加到当前模块扫描的路径里
from Utils.GetAppiumDriver import GetAppiumDriver

#导入WebDriverWait类库
from selenium.webdriver.support.ui import WebDriverWait
import time
class GetToastText(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver
    def GetToastValue(self,toast_msg):

        msg='//*[@text="{}"]'.format(toast_msg)

        Element_Toast=WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_element_by_xpath(msg))
        return Element_Toast