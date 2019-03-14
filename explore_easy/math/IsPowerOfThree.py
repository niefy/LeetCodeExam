"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/25/math/62/
题目：给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:
输入: 27
输出: true

进阶：
你能不使用循环或者递归来完成本题吗？

@author Niefy
@date 2018-11-21
"""


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        product= 1 #乘积
        while product<n:
            product=product*3
            if product==n:
                return True
        return False

    def isPowerOfThree1(self, n): #LeetCode高分解答
        """
        :type n: int
        :rtype: bool
        """
        maxThreeInt = 3 ** 19

        return n > 0 and maxThreeInt % n == 0

#测试代码
t=Solution()
print(t.isPowerOfThree(27))