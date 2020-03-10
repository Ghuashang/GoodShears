import os
import sys
os.getcwd()#返回当前进程的工作目录
sys.path.append(os.getcwd())#将模块路径加到当前模块扫描的路径里
#导入webdriver库
from appium import webdriver
from Utils.sing import singleton
#不需要传参，只能对此处修饰位单例模式
@singleton
class GetAppiumDriver():
    #构造函数（初始化函数），为其他模块提供服务，相当于定义一个全局
    def __init__(self):
        device_info = {}
        device_info['platformName'] = 'Android'  # 设备平台
        device_info['platformVersion'] = os.popen('adb shell getprop ro.build.version.release').read()  # 设备系统版本
        device_info["deviceName"] = os.popen('adb shell getprop ro.product.model').read()  # 设备名称
        device_info["device"] = os.popen('adb shell getprop ro.product.brand').read()  # 设备厂商信息
        device_info["app"] = "/Users/yenuo/Documents/专高6项目实战/案例应用程序/mncg.apk"  # app绝对路径
        device_info["noReset"] = True  # 是否重置应用
        device_info['chromedriverExecutable']="/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver"
        device_info['"appPackage"'] = 'com.jhss.youguu'
        device_info["appActivity"] = ".SplashActivity"  # app的活动页名称
        device_info['automationName'] = 'uiautomator2'  # 处理tosta提示业务
        # 使用webdrivr协议，远程（Remote）链接appium（'http://127.0.0.1:4723/wd/hub'）和设备(device_info)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_info)