"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/35/
题目：有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

@author Nifury
@date 2018-09-12
"""
class IsAnagram:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            temp=set(s)
            for x in temp:
                if s.count(x)!=t.count(x):
                    return False
        return True


#测试代码
t=IsAnagram()
print(t.isAnagram("anagram","nagaram"))
print(t.isAnagram("rat","car"))