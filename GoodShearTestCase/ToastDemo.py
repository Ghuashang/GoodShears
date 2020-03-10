# 导入webdriver库
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
#定义空字典
device_info={}
device_info['platformName']='Android'#设备平台
device_info['platformVersion']="6.0.1"#设备系统版本
device_info["deviceName"]="DUK_AL20"#设备名称
device_info["device"]="hlteuc"#设备厂商信息
device_info["app"]="/Users/yenuo/Documents/专高6项目实战/案例应用程序/mncg.apk"#app绝对路径
device_info["noReset"]=True#是否重置应用
device_info['"appPackage"']='com.jhss.youguu'
device_info["appActivity"]=".SplashActivity"#app的活动页名称
device_info['automationName']='uiautomator2'#处理tosta提示业务
#使用webdrivr协议，远程（Remote）链接appium（'http://127.0.0.1:4723/wd/hub'）和设备(device_info)
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',device_info)
time.sleep(7)
#点击"模拟炒股"图标
tipElement=driver.find_element_by_id("com.jhss.youguu:id/rl_bottom_tab")
tipElement.find_element_by_xpath("//*[@class='android.widget.ImageView' and @index='0']").click()
time.sleep(2)
#点击立即领取
driver.find_element_by_id("com.jhss.youguu:id/login_by_simulate").click()
time.sleep(2)
#点击登录按钮


driver.find_element_by_id("com.jhss.youguu:id/bt_login").click()
#预期结果
expValue="请输入手机号"
#获取toast
Toast=WebDriverWait(driver,10,0.5).until(lambda x:x.find_element_by_xpath("//*[@text='请输入手机号']"))
#Toast文本赋值给实际结果
actValue=Toast.text
#实际结果和预期是否一致
if actValue==expValue:
    print("pass")
else:
    print("Fail")
#结束清理

driver.quit()
'''
一条完整的自动化用例，包含一下部分
初始化
构造数据及执行过程
断言
结束清理
'''

