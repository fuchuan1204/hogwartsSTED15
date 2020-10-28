# author: fuchuan    time:2020-10-28
from selenium_wx.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = "霍格沃兹13x"
        account = "aaaaaah_hogwarts"
        phonenum = "13400000007"

        addmember = self.main.goto_addmember()
        addmember.add_member(username, account, phonenum)
        assert username in addmember.get_member(username)
