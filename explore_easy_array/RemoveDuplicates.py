"""
链接：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/21/
题目：从排序数组中删除重复项
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

说明:
为什么返回数值是整数，但输出的答案是数组呢?
请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
"""
class RemoveDuplicates:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                del nums[i]
            else:
                i = i + 1
        return len(nums)


# 测试代码
t = RemoveDuplicates()
array = [0,0,1,1,1,2,2,3,3,4]
len = t.removeDuplicates(array)
print('array=', array)
print('len=', len)
