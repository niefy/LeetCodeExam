"""
题目：1008. 先序遍历构造二叉树
返回与给定先序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。

(回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，值总 < node.val，而 node.right 的任何后代，值总 > node.val。此外，先序遍历首先显示节点的值，然后遍历 node.left，接着遍历 node.right。）


示例：
输入：[8,5,1,7,10,12]
输出：[8,5,10,1,7,null,12]
图：https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/03/08/1266.png
 

提示：
1 <= preorder.length <= 100
先序 preorder 中的值是不同的。


@author Niefy
@date 2019-03-12
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:#构造二叉树
        root=TreeNode(preorder[0])
        def addToTree(node,value):#将值添加到搜索树中
            if value<node.val:#需添加到左边
                if node.left==None:#左边为空直接添加
                    node.left=TreeNode(value)
                else: #左边不为空
                    addToTree(node.left,value)
            else:#需添加到右边
                if node.right==None:#右边为空直接添加
                    node.right=TreeNode(value)
                else:
                    addToTree(node.right,value)
        for i in range(1,len(preorder)):
            addToTree(root,preorder[i])
        return root
    
    def inorderTraversal(self, root):#将二叉树遍历显示
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
t=Solution()
res=t.bstFromPreorder([8,5,1,7,10,12])
print(t.inorderTraversal(res))