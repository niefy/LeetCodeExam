"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/31/linked-list/82/
题目：两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

@author Niefy
@date 2018-11-28
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        addition=0
        head=node=ListNode(0)
        while l1!=None or l2!=None:
            sum=addition
            if l1!=None:
                sum+=l1.val
                l1=l1.next
            if l2!=None:
                sum+=l2.val
                l2=l2.next
            if sum>=10:#进位
                addition=1
                sum-=10
            else:
                addition=0
            node.next=ListNode(sum)
            node=node.next
        if addition>0:
            node.next=ListNode(addition)
        return head.next

#测试代码
l1_head=l1=ListNode(2)
l1.next=ListNode(4)
l1=l1.next
l1.next=ListNode(3)

l2_head=l2=ListNode(5)
l2.next=ListNode(6)
l2=l2.next
l2.next=ListNode(9)

t=Solution()
result=  t.addTwoNumbers(l1_head,l2_head)
while result!=None:
    print(result.val,end='->')
    result=result.next
            