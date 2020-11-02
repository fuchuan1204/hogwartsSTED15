# author: fuchuan    time:2020-11-02
'''
获取包名和Activity
adb logcat |grep -i activitymanager

可以通过命令启动app
adb shell am start -n com.tencent.wework/.launch.LaunchSplashActivity
'''
import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class Testwx:
    def setup(self):
        desire_cap = {
            "platformName": "Android",
            "deviceName": "test",
            "noReset": True,  # 记住之前的动作，如首页弹框，第一次手动关闭后，第二次就不会在弹了
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            # "dontStopAppOnReset": True,  # 首次启动的时候，不停止app(停留在那个页面。还在哪个页面继续操作，不会从新启动app，需要手动执行操作，如返回上页面，不会会对下一条用例产生影响)
            "skipDeviceInitialization": True,  # 跳过安装，权限设置等操作
            "unicodeKeyboard": True,  # 可以输入中文
            "resetKeyboard": True,
            "settings[waitForIdleTimeout]": 0  # 无论这个页面是动态还是非动态，都会直接发送请求，不需要任何等待，完美提升了运行速度
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def test_wx(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/eas'and @text='工作台']").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("打卡").instance(0))').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"次外出")]').click()
        # time.sleep(2)
        # page_source打印页面结构信息，用之前在前面需要加强制等待时间
        # assert "外出打卡成功" in self.driver.page_source
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
