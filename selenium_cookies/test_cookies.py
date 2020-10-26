# author: fuchuan    time:2020-10-26
import shelve
from builtins import str
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By


class Testcookies:
    def setup(self):
        # 浏览器服用方法
        options = Options()
        options.debugger_address = '127.0.0.1:9222    '
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    # def teardown(self):
    #     self.driver.quit()
    # def test_login(self):
    #     self.driver.get('https://work.weixin.qq.com/')
    #     self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()

    def test_weixin(self):
        self.driver.find_element(By.ID, "menu_contacts").click()

    def test_cookie(self):
        # get_cookies() 可以获取当前打开的页面的cookies 信息
        # add_cookie() 可以把cookie 添加到当前的页面中去
        #  cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'Bc-U8qmU60X4y8EoZC7LEGnt_-p6qyfgprckmZ6jt7whMhklRmk0vJPpZJC9KNWU896_mcgdSvHFkW5yIKkkLnkFWUfEJjhH32kJjob6ujKT2OP1IVivfvY51JP5NVoCLgnvdrR_9xmKHoWNro0ylCNZzPl2LAbgSvtkz5_6_OEdHmednkcIxA6cc2558JMg_zos1h_9sQ44ibNY4pVJF-Ommsd7TJQXFC98MarrLBJs1EThn1y_6rsIEYpjrZy5otNzoRK0-4hrbIFmveoNcQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/',
             'secure': False, 'value': '1688852943220498'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/',
             'secure': False, 'value': '1688852943220498'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
             'secure': False, 'value': '1970325038160033'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'SVZJB9oHZ1eS2Ks2e9mK6X2oOne24mYOD7SZHJ__q9CJAiVPjM40hHZnGP2VnsvW'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/',
             'secure': False, 'value': 'a7125462'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/',
             'secure': False, 'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '3998755748'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635257569, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
             'value': '1603607234,1603687814,1603689793,1603721569'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False,
                                  'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/',
                                  'secure': False, 'value': '1603721569'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/',
             'secure': False, 'value': '1485363933768469'},
            {'domain': '.qq.com', 'expiry': 1603814167, 'httpOnly': False, 'name': '_gid', 'path': '/',
             'secure': False, 'value': 'GA1.2.619781242.1603606499'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603753104, 'httpOnly': True, 'name': 'ww_rtkey',
             'path': '/', 'secure': False, 'value': 'j4efob'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '1938009088'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1606319770, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1666799767, 'httpOnly': False, 'name': '_ga', 'path': '/',
             'secure': False, 'value': 'GA1.2.668025938.1599318114'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1630854110, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'}]

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def test_shelve(self):
        # shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库
        # 可以通过 key，value 来把数据保存到shelve中
        # 读取cookie
        db = shelve.open("cookies")
        cookies = db['cookie']

        # 利用读取的cookie 完成登录操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        # # 找到"导入联系人"按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # # 上传
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            r"C:\Users\riche\Desktop/mydata.xlsx")
        # # 验证 上传文件名
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "mydata.xlsx" == filename
        sleep(3)
