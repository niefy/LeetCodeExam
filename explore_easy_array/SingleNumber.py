"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/25/
题目：只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1
@author niefy
@date 2018-09-11
"""


class SingleNumber:
    def singleNumber_1(self, nums):  # 使用字典记录数字出现次数
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        for x in nums:
            if x in map:
                map[x] = 2
            else:
                map[x] = 1
        for key in map.keys():
            if map[key] == 1:
                return key
        return None

    def singleNumber_2(self, nums):  # LeetCode最佳算法：去重求和*2-原数组求和
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums))*2-sum(nums)

# 测试代码
t = SingleNumber()
nums = [2, 2, 1]
#print(t.singleNumber(nums))
print(t.singleNumber_2(nums))