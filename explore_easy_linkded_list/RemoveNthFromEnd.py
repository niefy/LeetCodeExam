"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/42/\
题目：删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？

@author niefy
@date 2018-09-17
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class RemoveNthFromEnd:
    def removeNthFromEnd(self, head, n):#使用数组存放
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            return None
        array = []
        node = head
        while node != None:
            array.append(node)
            node = node.next
        delIndex = len(array) - n
        print('删除节点序号', delIndex)
        if delIndex > 0:
            array[delIndex - 1].next = array[delIndex].next
        else:
            head = array[1]
        return head
