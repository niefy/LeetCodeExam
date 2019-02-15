"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/52/design/110/
题目： Insert Delete GetRandom O(1)
设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。

insert(val)：当元素 val 不存在时，向集合中插入该项。
remove(val)：元素 val 存在时，从集合中移除该项。
getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。

@author Niefy
@date 2019-02-15
"""
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set= []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            return False
        self.set.append(val)
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            self.set.remove(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.set)
        
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.set)
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.set)
print(obj.getRandom())



