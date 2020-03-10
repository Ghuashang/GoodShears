import os
import sys
os.getcwd()#返回当前进程的工作目录
sys.path.append(os.getcwd())#将模块路径加到当前模块扫描的路径里
import os
import sys
os.getcwd()#返回当前进程的工作目录
sys.path.append(os.getcwd())#将模块路径加到当前模块扫描的路径里
from Utils.GetAppiumDriver import GetAppiumDriver
from selenium.webdriver.common.by import By
class GetPageElement():
    def __init__(self):
        self.driver = GetAppiumDriver().driver
    def Page_Element(self,type,revValue,fileName,ErrTips):
        # if num==():
        try:
            if type=="id":
                GetElement=self.driver.find_element_by_id(revValue)
            elif type=="class":
                GetElement=self.driver.find_element_by_class_name(revValue)
            elif type=="name":
                GetElement=self.driver.find_element_by_name(revValue)
            elif type=="xpath":
                GetElement=self.driver.find_element_by_xpath(revValue)
            return GetElement
        except Exception as err:
            self.driver.get_screenshot_as_file("/Users/yenuo/PycharmProjects/GoodShears/Testresult/PageIMG/"+fileName+".png")
            # self.driver.save_screenshot()
            assert False,ErrTips
        #     except Exception as err:#捕获基本错误类存储到内存空间
        #         #获取具体错误并处理
        #         assert False,""
        # else:
        #     if type=="id":
        #         GetElements=self.driver.find_elements_by_id(revValue)[num]
        #     elif type=="class":
        #         GetElements=self.driver.find_elements_by_class_name(revValue)[num]
        #     elif type=="name":
        #         GetElements=self.driver.find_elements_by_name(revValue)[num]
        #     elif type=="xpath":
        #         GetElements=self.driver.find_elements_by_xpath(revValue)[num]
        #     return GetElements


