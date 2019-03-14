"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/24/
题目：存在重复
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:
输入: [1,2,3,1]
输出: true

@author Niefy
@date 2018-09-11
"""
class ContainsDuplicate:

    def containsDuplicate_1(self, nums):#使用集合查找记录
        """
        :type nums: List[int]
        :rtype: bool
        """
        map=set()
        for x in nums:
            if x in map:
                return True
            else:
                map.add(x)
        return False

    def containsDuplicate_2(self, nums):#使用集合查找记录
        """
        :type nums: List[int]
        :rtype: bool
        """
        if(len(nums)==len(set(nums))):
            return False
        else:
            return True

#测试代码
t=ContainsDuplicate()
array=[1,2,3,1]
print(t.containsDuplicate_1(array))

print(t.containsDuplicate_2(array))