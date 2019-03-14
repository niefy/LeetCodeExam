"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/78/
题目：给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

@author Niefy
@date 2018-11-27
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={}
        i=0
        longestLen=0
        while i <len(s):
            char=s[i]
            if char in dict:#检测到重复值就记录当前长度，然后跳回到重复字母的下一个位置继续
                i=dict[char]+1
                longestLen=max(longestLen,len(dict))
                dict={}
            else:
                dict[char]=i
                i+=1
        longestLen=max(longestLen,len(dict))
        return longestLen


t=Solution()
print('最长字串：',t.lengthOfLongestSubstring("abcabcbb"))