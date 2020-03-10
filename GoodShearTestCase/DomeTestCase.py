
#导入webdriver类库（链接appium和设备需要用到webdriver协议）
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
# from time import sleep
#定义一个空字典，列表或字典称为存储器（存放设备信息）
device_info={}
device_info['platformName']='Android'#设备平台
device_info['platformVersion']="6.0.1"#设备系统版本
device_info["deviceName"]="DUK_AL20"#设备名称
device_info["device"]="hlteuc"#设备厂商信息
device_info["app"]="/Users/yenuo/Documents/专高6项目实战/案例应用程序/mncg.apk"#app绝对路径
device_info["noReset"]=True#是否重置应用
device_info['"appPackage"']='com.jhss.youguu'
device_info["appActivity"]=".SplashActivity"#app的活动页名称
device_info['automationName']='uiautomator2'
#使用webdrivr协议，远程（Remote）链接appium（'http://127.0.0.1:4723/wd/hub'）和设备(device_info)
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',device_info)
time.sleep(5)
#尝试
try:
    #查找关闭按钮，找到做点击操作
    driver.find_element_by_id("com.jhss.youguu:id/iv_ad_close").click()
except:
    pass
    # time.sleep(2)
    # try:
    #     driver.find_element_by_id("com.jhss.youguu:id/close_btn").click()
    # except:
    #     pass
# 点击模拟炒股页面"学习"按钮
# driver.find_element_by_xpath("//android.widget.TextView[@text=\"学习\"]").click()
# driver.find_element_by_xpath("//android.widget.TextView[@id=\"com.jhss.youguu:id/tv_study\"]").click()
# driver.find_element_by_xpath("//*[@text='学习' and @index=\"2\"]").click()
# driver.find_element_by_xpath("//*[@text='学习' and @id=\"com.jhss.youguu:id/tv_study\"]").click()
# # driver.tap([(597,710)])
# time.sleep(2)
driver.find_element_by_id("com.jhss.youguu:id/login_by_simulate").click()
time.sleep(2)
driver.find_element_by_id("com.jhss.youguu:id/bt_login").click()
toast_message = "请输入手机号"
message ='//*[@text=\'{}\']'.format(toast_message)
toast_element = WebDriverWait(driver,10,0.5).until(lambda x:x.find_element_by_xpath(message))
print(toast_element.text)



