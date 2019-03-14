"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/50/sorting-and-searching/102/
题目：搜索旋转排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

@author Niefy
@date 2018-12-13
"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not len(nums):
            return -1
        i=0
        if nums[i]>target:#从后往前搜索
            i=len(nums)-1
            while i>0 and nums[i]>target:
                i-=1
        elif nums[i]<target:#从前往后搜索
            while i<len(nums) and nums[i]<target:
                i+=1
        if i>=0 and i<len(nums) and nums[i]==target:
            return i
        else:
            return -1
# 测试代码
t=Solution()
nums = [4,5,6,7,0,1,2]
print(t.search(nums,0))
print(t.search(nums,3))
print(t.search([1],0))
print(t.search([1],2))