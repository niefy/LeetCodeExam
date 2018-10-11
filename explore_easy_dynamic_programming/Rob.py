"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/23/dynamic-programming/57/
题目：打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

@author Niefy
@date 2018-10-11
"""
class Rob:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        if length<1:
            return 0
        elif length==1:
            return nums[0]
        elif length==2:
            return max(nums[0],nums[1])

        #长度大于3
        sum1=nums[0]
        sum2=max(nums[0],nums[1])
        for i in range(2,length):
            sumI=max(sum1+nums[i],sum2)
            sum1=sum2
            sum2=sumI
        return sum2

#测试代码
t=Rob()
nums=[2,7,9,3,1]
print(t.rob(nums))

