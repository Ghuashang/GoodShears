# 导入单元测试框架和时间类库\paramunittest
import unittest,time,paramunittest
import os
import sys
os.getcwd()#返回当前进程的工作目录
sys.path.append(os.getcwd())#将模块路径加到当前模块扫描的路径里
from Utils.PythonHlepApi import PythonHelpApi
#导入GetAPpiumDriver 类（因为这个模块要用到slef.drier）
from Utils.GetAppiumDriver import GetAppiumDriver#来至于Utils包下面的GetAppiumDriver模块导入GetAppiumDriver类
from Common.LoginModel import LoginModel
from Common.GetToastText import GetToastText
from Utils.GetPageElement import GetPageElement

#定义一个类并继承TestCase类
class test_User_Login(unittest.TestCase):
    @classmethod#修饰以类的方式运行
    def setUpClass(cls) -> None:#只运行一次，最先运行
        # 类的实例化调属性
        cls.driver = GetAppiumDriver().driver
        time.sleep(7)
        # tipElement = cls.driver.find_element_by_id("com.jhss.youguu:id/rl_desktop_trade_new")
        # tipElement.find_element_by_xpath("//*[@class='android.widget.ImageView' and @index='0']").click()
        time.sleep(2)
        cls.driver.find_element_by_id("com.jhss.youguu:id/login_by_simulate").click()
        time.sleep(2)
    @classmethod#修饰以类的方式结束
    def tearDownClass(cls) -> None:#只运行一次，最后运行

        GetAppiumDriver().driver.quit()

    #继承TestCase中初始化方法
    def setUp(self) -> None:
        pass
    """手机号为空，登录的Toast提示"""
    def test_login0001(self):
        LoginModel().Login_PhoneAndCode("","")
        expValue="请输入手机号"
        actValue=GetToastText().GetToastValue("请输入手机号").text
        self.assertEqual(actValue,expValue)

    """验证码为空，登录的Toast提示"""
    def test_login0002(self):
        LoginModel().Login_PhoneAndCode("13526042776","")
        expValue = "请输入验证码"
        actValue = GetToastText().GetToastValue("请输入验证码").text
        self.assertEqual(actValue, expValue)

    """验证码错误，登录的Toast提示"""
    def test_login0003(self):
        LoginModel().Login_PhoneAndCode("13526042776","1234")
        expValue = "验证码不正确或已过期"
        actValue = GetToastText().GetToastValue("验证码不正确或已过期").text
        self.assertEqual(actValue, expValue)
    """输出1707AMobileAutoTest"""
    def test_login0004(self):
        print("1707AMobileAutoTest")

    #继承TestCase中结束清理方法
    def tearDown(self) -> None:
        pass

# if __name__ == '__main__':
#     #继承main函数组织并管理用例运行
#     # unittest.main()
#     #定义一个测试套件
#     LoginSUite=unittest.TestSuite()
#     #定义一个列表
#     suiteList=["test_login0004","test_login0001","test_login0002"]
#
#     #添加用例到测试套件
#     for tmp in suiteList:
#         LoginSUite.addTest(test_User_Login(tmp))
#     # LoginSUite.addTest(test_User_Login("test_login0004"))
#     # LoginSUite.addTest(test_User_Login("test_login0001"))
#     # LoginSUite.addTest(test_User_Login("test_login0003"))
#     # 运行测试套件
#     unittest.TextTestRunner().run(LoginSUite)



