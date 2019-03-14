"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/24/design/59/
题目：设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

@author Niefy
@date 2018-11-19
"""

class StackNode:
    def __init__(self,val,next):
        self.val=val
        self.next=next
        if next is None:
            self.min=val
        else:
            self.min=min(val,next.min)

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.topNode=None


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        temp=self.topNode
        newNode=StackNode(x,temp)
        self.topNode=newNode


    def pop(self):
        """
        :rtype: void
        """
        self.topNode=self.topNode.next

    def top(self):
        """
        :rtype: int
        """
        return self.topNode.val

    def getMin(self):
        """
        :rtype: int
        """
        return self.topNode.min

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(1)
obj.push(5)
print(obj.top())
print('最小',obj.getMin())
# obj.push(x)
obj.pop()
print(obj.top())
print('最小',obj.getMin())
# param_3 = obj.top()
# param_4 = obj.getMin()