"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/53/math/114/
题目：Excel表列序号
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701

@author Niefy
@date 2018-01-15
"""
class Solution:
    def charToNum(self,char):
        return ord(char)-64

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n=len(s)
        res=0
        for k in s:
            res+=self.charToNum(k)*(26**(n-1))
            n-=1
        return res


#测试代码
t=Solution()
print('A=',t.charToNum('A'))
print('B=',t.charToNum('B'))
print('Z=',t.charToNum('Z'))

print(t.titleToNumber('A'))
print(t.titleToNumber('AB'))
print(t.titleToNumber('ZY'))
print(t.titleToNumber('ZYUA'))