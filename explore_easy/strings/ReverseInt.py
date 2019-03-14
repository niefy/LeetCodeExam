"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/33/
题目： 颠倒整数
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:
输入: 123
输出: 321

 示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储 32 位有符号整数。根据这个假设，如果反转后的整数溢出，则返回 0。

@author Niefy
@date 2018-09-12
"""

class ReverseInt:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result=None
        if (x >= 0):
            result= int(str(x)[::-1])
        else:
            result = 0 - int(str(-x)[::-1])
        if result > 2**31-1 or result < -(2**31):
            return 0
        else:
            return result


# 测试代码
t = ReverseInt()
print('int最大值：',2**31-1)
print(t.reverse(1534236469))
