"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/27/
题目：加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

@author Nifury
@date 2018-09-12
"""

class PlusOne:
    def plusOne(self, digits):#从后往前加即可
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=len(digits)-1
        while i>=0:
            if digits[i]<9:#不需要进位
                digits[i] += 1
                break
            elif i>0:#非第一位发生进位
                digits[i]=0
                i-=1
            else:#第一位发生进位
                digits[i] = 0
                digits.insert(0,1)
                break
        return digits


t=PlusOne()
array = [1,2,3]
result = t.plusOne(array)
print(result)