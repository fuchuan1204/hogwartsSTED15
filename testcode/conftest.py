# author: fuchuan    time:2020-10-22
import pytest
from testcode.Calculator import Calculator
import pytest


@pytest.fixture(scope='module')
def cal():
    calc = Calculator()
    print("计算开始")
    yield calc
    print("结束计算")


@pytest.fixture(scope='module')
def login():
    username = "ff"
    print("登录操作")
    yield username
    print("登出操作")
