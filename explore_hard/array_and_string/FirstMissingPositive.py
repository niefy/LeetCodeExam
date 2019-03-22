"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-hard/55/array-and-strings/128/
题目：第一个缺失的正数
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:
输入: [1,2,0]
输出: 3

示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

@author Niefy
@date 2019-03-22
"""

class Solution:
    def firstMissingPositive(self, nums) -> int:#构建布尔数组array，如果正整数n出现则array[n-1]=True,找到第一项为False的,空间复杂度不为常数
        countPosstive=0
        for n in nums:#统计正整数个数
            if n>0 :
                countPosstive+=1
        
        array=[False]*countPosstive
        for n in nums:
            if n>0 and n<=countPosstive:
                array[n-1]=True
        print(array)
        for i in range(len(array)):
            if not array[i]:
                return i+1
        return len(array)+1
    
    def firstMissingPositive_1(self, nums):#来自LeetCode用户解答(直接从1尝试)
        """
        :type nums: List[int]
        :rtype: int
        """
        n=1
        while n in nums:
            n=n+1
        return n




# 测试代码
t=Solution()
print(t.firstMissingPositive_1([1,2,0,-1]))
# print(t.firstMissingPositive_1([3,4,-1,1]))
# print(t.firstMissingPositive_1([7,8,9,11,12]))
# print(t.firstMissingPositive_1([1,2,3,4]))
# print(t.firstMissingPositive_1([]))
