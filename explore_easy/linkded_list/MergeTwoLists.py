"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/44/
题目：合并两个有序链表
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

@author Niefy
@date 2018-09-20
"""
class MergeTwoLists:
    def mergeTwoLists(self, l1, l2):#遍历取小
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
            # 确定head
        head = None
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        print('head:', head.val)
        # 排序遍历
        node = head
        while l1 != None or l2 != None:
            if l1 == None:
                node.next = l2
                break
            elif l2 == None:
                node.next = l1
                break
            elif l1.val <= l2.val:
                node.next = l1
                node = l1
                l1 = l1.next
            else:
                node.next = l2
                node = l2
                l2 = l2.next
        return head