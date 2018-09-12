"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/23/
题目：旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。

@author niefy
@date 2018-09-11
"""


class Rotate:
    def rotate_1(self, nums, k):# 未修改原数组
        splitIndex=len(nums)-k
        result=nums[splitIndex:len(nums)]+nums[0:splitIndex]
        return result

    def rotate_2(self, nums, k):#遍历移动
        for i in range(0,k):
            item=nums.pop()
            nums.insert(0,item)

    def rotate_3(self, nums, k):#分段移动
        splitIndex = len(nums) - k
        temp = nums[0:splitIndex]
        del nums[0:splitIndex]
        nums.extend(temp)


# 测试代码
t=Rotate()
array = [1,2,3,4,5,6,7]
#result = t.rotate_1(array,3)
#print('方法一结果：',result)

#t.rotate_2(array,3)
#print(array)

t.rotate_3(array,3)
print(array)
