import os

deviceName = os.popen('adb shell getprop ro.product.model').read()
print(deviceName)
platformVersion = os.popen('adb shell getprop ro.build.version.release').read()
print(platformVersion)
device = os.popen('adb shell getprop ro.product.brand').read()
print(device)