"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/79/
题目：最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

@author Niefy
@date 2018-11-27
"""
class Solution:
    def longestPalindrome(self, s):#基础版，顺序往前检测
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        s='|'.join(s)
        result=''
        sLen=len(s)
        i=0
        while i<sLen:
            k=1
            while i-k>=0 and i+k<sLen and s[i-k]==s[i+k]:
                if '|'!=s[i-k]:
                    temp=s[i-k:i+k+1]
                    if len(temp)>len(result):
                        result=temp   
                k+=1
            i+=1
        return result.replace('|','')


    def longestPalindrome1(self, s):#改良版，从中间往两边检测
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        s='|'.join(s)
        result=''
        sLen=len(s)
        mid=int(sLen/2) #从中间往两边测试
        i=mid
        while i<sLen:
            k=1
            while i-k>=0 and i+k<sLen and s[i-k]==s[i+k]:
                print('i=',i,'k=',k)
                if '|'!=s[i-k]:
                    temp=s[i-k:i+k+1]
                    if len(temp)>len(result):
                        result=temp
                k+=1
            k-=1 #还原循环末尾多执行的自增
            if i-k==0 or i+k==sLen-1: #一直到头都是回文序列，必是最长字串
                break
            if i<=mid:
                i=mid+(mid-i)+1
            else:
                i=mid-(i-mid)
        return result.replace('|','')

#测试代码
t=Solution()
# print('result=',t.longestPalindrome("babad"))
print('result=',t.longestPalindrome1("abb"))
# print('result=',t.longestPalindrome("bb"))
#print(t.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))