"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-hard/55/array-and-strings/123/
题目：Product of Array Except Self
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

@author Niefy
@date 2019-03-14
"""
class Solution:
    def productExceptSelf(self, nums): #第n项结果=此元素前几项的乘积*此元素后几项的乘积
        if len(nums)<2:
            return []
        productPlain=[None]*len(nums) #正序乘积：[nums[1],nums[1]*nums[2],nums[1]*nums[2]*nums[3],...]
        p=1
        for i in range(0,len(nums)):
            p=p*nums[i]
            productPlain[i]=p
        print('正序累乘：',productPlain)

        productReverse=[None]*len(nums) #反序乘积(从后往前乘):[...,nums[n-3]*nums[n-2]*nums[n-1],nums[n-2]*nums[n-1],nums[n-1]]
        p=1
        for i in range(len(nums)-1,-1,-1):
            p=p*nums[i]
            productReverse[i]=p
        print('倒序累乘：',productReverse)

        res=[None]*len(nums)
        res[0]=productReverse[1] #第一项和最后一项要单独处理
        for i in range(1,len(nums)-1):
            res[i]=productPlain[i-1]*productReverse[i+1]
        res[len(nums)-1]=productPlain[len(nums)-2] #第一项和最后一项要单独处理
        return res

    def productExceptSelf1(self, nums): #productExceptSelf方法简化（不需要预先同时存储正序和反序乘积,直接一步到位存储到res）
        res=[1]*len(nums)
        p=1
        for i in range(1,len(nums)):
            p=p*nums[i-1]
            res[i]=p
        p=1
        for i in range(len(nums)-2,-1,-1):
            p=p*nums[i+1]
            res[i]*=p
        return res
# 测试代码
t=Solution()
# print(t.productExceptSelf([1,2,3,4]))
# print(t.productExceptSelf([1]))
# print(t.productExceptSelf([3,7,2,8]))
# print(t.productExceptSelf([5,5,5,5]))

print(t.productExceptSelf1([1,2,3,4]))
print(t.productExceptSelf1([1]))
print(t.productExceptSelf1([3,7,2,8]))
print(t.productExceptSelf1([5,5,5,5]))