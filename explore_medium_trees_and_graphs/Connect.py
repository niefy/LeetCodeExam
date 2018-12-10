"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/32/trees-and-graphs/88/
题目：每个节点的右向指针
给定一个二叉树

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

说明:

你只能使用额外常数空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
你可以假设它是一个完美二叉树（即所有叶子节点都在同一层，每个父节点都有两个子节点）。
示例:

给定完美二叉树，

     1
   /  \
  2    3
 / \  / \
4  5  6  7
调用你的函数后，该完美二叉树变为：

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL

@author Niefy
@date 2018-12-06
"""
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root): #以每一层的第一个节点为头，利用next指针遍历当前层，遍历时给下一层添加next指针
        """
        :type root: TreeNode
        """
        if not root:
            return
        levelHead=root #每一层的第一个节点
        while levelHead:#遍历层
            node=levelHead
            breakNode=None
            while node: #遍历一层内的节点
                if node.left:#完美二叉树，有left必定有right
                    if breakNode:
                        breakNode.next=node.left
                    node.left.next=node.right
                    breakNode=node.right
                node=node.next
            levelHead=levelHead.left

        
        
            


#测试代码
root=TreeLinkNode(1)
leftN=TreeLinkNode(2)
rightN=TreeLinkNode(3)
root.left=leftN
root.right=rightN
t=Solution()
t.connect(root)
print(leftN.next)