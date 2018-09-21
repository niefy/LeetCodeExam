"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/7/trees/50/
题目：二叉树的层次遍历
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

@author Niefy
@date 2018-09-21
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class LevelOrder:
    def levelOrder(self, root):#广度优先遍历，使用queue队列
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        pQueue = [root]
        cQueue = []
        result = []
        tempResult = []
        while True:
            if len(pQueue) > 0:  # 遍历某一层
                node = pQueue.pop(0)
                tempResult.append(node.val)
                if node.left:
                    cQueue.append(node.left)
                if node.right:
                    cQueue.append(node.right)
            elif len(cQueue) > 0:  # 某一层遍历完成，准备遍历下一层
                result.append(tempResult)
                pQueue = cQueue
                cQueue = []
                tempResult = []
            else:  # 全部遍历完成
                result.append(tempResult)
                break
        return result

