# author: fuchuan    time:2020-09-13
'''
    课后作业
    1、补全计算器（加法 除法）的测试用例
    2、使用参数化完成测试用例的自动生成
    3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
    注意：
    使用等价类，边界值，因果图等设计测试用例
    测试用例中添加断言，验证结果
    灵活使用 setup(), teardown() , setup_class(), teardown_class()

'''

import pytest
from test.Calculator import Calculator


class TestCacl:
    def setup(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [100, 200, 300], [0.1, 0.1, 0.2], [-1, -1, -2], [1, 0, 1]],
                             ids=['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case'])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[0.1, 0.1, 0.2], [0.1, 0.2, 0.3]], ids=['float1_case', 'float2_case'])
    def test_add_float(self, a, b, expect):
        result = self.calc.add(a, b)
        # 2代表的是小数点后边保留2位
        assert round(result, 2) == expect

    def test_div_zero(self):
        with pytest.raises(ZeroDivisionError):
            result = self.calc.div(1, 0)

    @pytest.mark.parametrize('a,b,expect', [[2, 1, 1], [200, 50, 150], [0.5, 0.2, 0.3], [-2, -1, -1]],
                             ids=['int_case', 'bignum_case', 'float_case', 'minus_csae'])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [0.1, 0.1, 0.2], [-1, -1, 1],
        [1, 0.2, 0.2]
    ], ids=['int_case', 'float_case', 'minus_case', 'zero_case'])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [
        [6, 2, 3], [-6, -2, -3], [100, 50, 20]], ids=['int_case', 'minus_case', 'bignum_case'])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect
    # @pytest.mark.parametrize('a,b,expect',[0.1,0.2,0.3])
    # def test_div1(self,a,b,expect):
    #     result = self.calc.div(a,b)
    #     assert result == expect
