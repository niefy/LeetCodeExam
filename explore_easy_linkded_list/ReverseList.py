"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/43/
题目：反转链表
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

@author Niefy
@date 2018-09-20
"""
class ReverseList:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        node = head
        temp1 = head.next
        node.next = None
        while temp1 != None:
            temp2 = temp1.next
            temp1.next = node
            node = temp1
            temp1 = temp2
        return node

