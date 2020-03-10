import unittest
import os
import sys
os.getcwd()#返回当前进程的工作目录
sys.path.append(os.getcwd())#将模块路径加到当前模块扫描的路径里
#多模块测试套件导入到模块（而不是导入类）
from Utils.PythonHlepApi import PythonHelpApi
from GoodShearTestCase import test_User_Login,test_reg_user
def MoreModelSuite():
    #定义测试套件
    MoreSUite=unittest.TestSuite()
    #添加用例到测试套件

    MoreSUite.addTest(unittest.makeSuite(test_User_Login.test_User_Login))
    MoreSUite.addTest(unittest.makeSuite(test_reg_user.test_reg_user))
    # unittest.TextTestRunner().run(MoreSUite)
    Title="登录和注册相关功能用例"
    Des="登录第一条用例验证用户名为空的toast提示信息，登录第二条用例验证验证码为空的toast提示信息。。。。。。"
    PythonHelpApi().CreatHTMLReport("LoginAndReg",Title,Des,MoreSUite)
MoreModelSuite()

