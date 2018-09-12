"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/36/
题目：验证回文字符串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false

@author niefy
@date 2018-09-12
"""
import re
class IsPalindrome:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=re.sub(r'\W', "", s).lower()
        print("去除符号空格转小写："+s1)
        return s1==s1[::-1]

#测试代码
t=IsPalindrome()
print()
print(t.isPalindrome("A man, a plan, a canal: Panama"))