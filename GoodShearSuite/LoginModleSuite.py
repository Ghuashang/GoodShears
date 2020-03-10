import unittest
import os
import sys
os.getcwd()#返回当前进程的工作目录
sys.path.append(os.getcwd())#将模块路径加到当前模块扫描的路径里
#单一模块测试套件导入到类
from GoodShearTestCase.test_User_Login import test_User_Login
#定义自定义函数
def LoginModel():
    # 定义一个测试套件
    LoginSUite=unittest.TestSuite()
    #定义一个列表
    suiteList=["test_login0004","test_login0001","test_login0002"]
    #添加用例到测试套件
    for tmp in suiteList:
        LoginSUite.addTest(test_User_Login(tmp))
    unittest.TextTestRunner().run(LoginSUite)

LoginModel()