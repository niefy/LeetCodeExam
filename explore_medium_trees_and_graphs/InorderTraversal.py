"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/32/trees-and-graphs/85/
题目：中序遍历二叉树
给定一个二叉树，返回它的中序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

前序、中序和后续遍历：https://www.cnblogs.com/turnips/p/5096578.html
@author Niefy
@date 2018-12-06
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        if not root:
            return result
        if root.left:
            result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result




#测试代码
root=TreeNode(1)
nodeR=TreeNode(2)
root.right=nodeR
nodeL=TreeNode(3)
nodeR.left=nodeL
t=Solution()
print(t.inorderTraversal(root))