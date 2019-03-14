"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/32/
题目： 反转字符串
编写一个函数，其作用是将输入的字符串反转过来。

示例 1:
输入: "hello"
输出: "olleh"

示例 2:
输入: "A man, a plan, a canal: Panama"
输出: "amanaP :lanac a ,nalp a ,nam A"

@author Niefy
@date 2018-09-12
"""
class ReverseString:
    def reverseString_1(self, s):#转为数组 -> 反转 -> 转为字符串
        """
        :type s: str
        :rtype: str
        """
        return ''.join((list(s)[::-1]))

    def reverseString_2(self, s):#LeetCode最佳
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

# 测试代码
t=ReverseString()
print(t.reverseString_1("hello"))
print(t.reverseString_2("hello"))