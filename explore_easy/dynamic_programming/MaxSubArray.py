"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/23/dynamic-programming/56/
题目：最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

@author Niefy
@date 2018-10-10
"""
class MaxSubArray:

    def maxSubArray(self, nums):#动态规划方法
        """
        参考：https://blog.csdn.net/zwzsdy/article/details/80029796
        :param nums: List[int]
        :return:
        """
        sum=nums[0]
        n=nums[0]
        i=1
        while i<len(nums):
            if n>0:
                n=n+nums[i]
            else:
                n=nums[i]
            print('n=',n,',sum=',sum)
            if sum<n:
                sum=n
            i+=1

        return sum


#测试代码
nums=[8,-19,5,-4,20]
t=MaxSubArray()
print('结果：',t.maxSubArray1(nums))


