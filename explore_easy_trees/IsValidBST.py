"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/7/trees/48/
题目：验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

@author Niefy
@date 2018-09-21
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class NodeInfo:#定义节点信息
    def __init__(self,valid,childMin,childMax):
        self.valid=valid
        self.childMin=childMin
        self.childMax=childMax

class IsValidBST:
    def isValidBST(self, root):#使用递归遍历判断
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.getNodeInfo(root).valid

    def getNodeInfo(self,node):
        """
        :type root: TreeNode
        :rtype: NodeInfo
        """
        if node==None:
            return None
        if node.left==None and node.right==None:
            return NodeInfo(True,node.val,node.val)
        elif node.left and node.right==None:
            leftInfo=self.getNodeInfo(node.left)
            return NodeInfo(leftInfo.valid and leftInfo.childMax<node.val,
                            min(leftInfo.childMin,node.val),
                            max(leftInfo.childMax,node.val))
        elif node.left==None and node.right:
            rightInfo = self.getNodeInfo(node.right)
            return NodeInfo(rightInfo.valid and rightInfo.childMin > node.val,
                            min(rightInfo.childMin, node.val),
                            max(rightInfo.childMax, node.val))
        else:#左右都不为None
            leftInfo = self.getNodeInfo(node.left)
            rightInfo = self.getNodeInfo(node.right)
            return NodeInfo(leftInfo.valid and rightInfo.valid and leftInfo.childMax<node.val and rightInfo.childMin > node.val,
                            min(leftInfo.childMin,rightInfo.childMin, node.val),
                            max(leftInfo.childMax,rightInfo.childMax, node.val))


