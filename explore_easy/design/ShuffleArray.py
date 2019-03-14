"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/24/design/58/
题目：打乱一个没有重复元素的数组。

示例：
// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();

@author Niefy
@date 2018-11-19
"""
import random

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        self.copy=nums.copy()

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):#执行超过时间，此方式为每次全部打乱
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        array = self.nums[:]
        length=len(array)
        k=0
        while k<length:
            rand1=random.randrange(length)
            temp=array[rand1]
            rand2=random.randrange(length)
            array[rand1]=array[rand2]
            array[rand2]=temp
            k+=1
        return array

    def shuffle1(self):#执行超过时间，此方式每次只打乱其中两个
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        length=len(self.copy)
        if length>2:
            randomIndex=random.randrange(0,length-1)
            self.copy[randomIndex],self.copy[randomIndex+1]=self.copy[randomIndex+1],self.copy[randomIndex]#交换值

        return self.copy

    def shuffle2(self):
        random.shuffle(self.copy)
        return self.copy

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# 测试
t=Solution([1,2,3])
k=0
while k<10:
    print(t.shuffle1())
    k+=1

print(t.reset())