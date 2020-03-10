import os
import sys
os.getcwd()#返回当前进程的工作目录
sys.path.append(os.getcwd())#将模块路径加到当前模块扫描的路径里
from Utils.GetAppiumDriver import GetAppiumDriver
from Utils.GetPageElement import GetPageElement
from Utils.PythonHlepApi import PythonHelpApi
import time
class LoginModel(object):
    def __init__(self):
        self.driver=GetAppiumDriver().driver
    def Login_PhoneAndCode(self,revUserName,revCode):
        ElementMethod=PythonHelpApi().readExcelData("loginPagey",1,1)
        ElementValue=PythonHelpApi().readExcelData("loginPagey",1,2)
        IMGInfo=PythonHelpApi().readExcelData("loginPagey",1,4)
        ErrToast=PythonHelpApi().readExcelData("loginPagey",1,5)
        GetPageElement().Page_Element("id", "com.jhss.youguu:id/et_username", "UserName_inpnt","登录页面的登录输入框未找到").send_keys(revUserName)
        GetPageElement().Page_Element("id", "com.jhss.youguu:id/et_password", "Login_code_input","登录页面验证码输入框未被定位到").send_keys(revCode)
        GetPageElement().Page_Element(ElementMethod, ElementValue, IMGInfo, ErrToast).click()
