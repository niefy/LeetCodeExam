"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/31/linked-list/84/
题目：相交链表
编写一个程序，找到两个单链表相交的起始节点。

例如，下面的两个链表：
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
在节点 c1 开始相交。

注意：
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

@author Niefy
@date 2018-12-03
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):#将其中一个链表的放到list中,遍历另一链表检查(LeetCode提交超出时间限制)
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        list=[]
        A=headA
        while A:
            list.append(A)
            A=A.next
        B=headB
        while B:
            if B in list:
                return B
            B=B.next
        return None

    def getIntersectionNode1(self, headA, headB):#将其中一个链表的节点地址项放到字典中
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        dict={}
        A=headA
        while A:
            dict[id(A)]=True
            A=A.next
        B=headB
        while B:
            if id(B) in dict:
                return B
            B=B.next
        return None

        