"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/7/trees/47/
题目：二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

@author Niefy
@date 2018-09-21
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class MaxDepth:
    def maxDepth(self, root):  # 深度优先遍历
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        node = root
        if node.left == None and node.right == None:
            return 1
        else:#未到最底层需要递归遍历
            return max(self.maxDepth(node.left),self.maxDepth(node.right)) + 1