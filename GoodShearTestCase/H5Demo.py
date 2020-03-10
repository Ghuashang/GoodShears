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
device_info["chromedriverExcutable"]="/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver"
#使用webdrivr协议，远程（Remote）链接appium（'http://127.0.0.1:4723/wd/hub'）和设备(device_info)
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',device_info)
time.sleep(7)
#尝试
try:
    #查找关闭按钮，找到做点击操作
    driver.find_element_by_id("com.jhss.youguu:id/iv_ad_close").click()
except:
    pass
driver.find_element_by_id('com.jhss.youguu:id/btn_desktop_discovery').click()
time.sleep(3)
driver.find_element_by_id("com.jhss.youguu:id/ll_bottom_menu").click()

# driver.find_element_by_id("com.jhss.youguu:id/tv_study").click()
time.sleep(2)
print(driver.contexts)
time.sleep(1)
# driver.switch_to.context("WEBVIEW_com.jhss.youguu")
driver.switch_to.context("WEBVIEW_com.jhss.youguu")

driver.find_element_by_name("hy").click()

