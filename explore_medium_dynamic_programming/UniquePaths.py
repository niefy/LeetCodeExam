"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/51/dynamic-programming/105/
题目：不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？

https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/robot_maze.png

例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:
输入: m = 7, n = 3
输出: 28

@author Niefy
@date 2018-12-13
"""
class Solution:
    def uniquePaths(self, m, n):
        """
        需要往右：m-1次，往下n-1次，其实就是在（m-1+n-1）步中选（m-1)项往右，其余往下走，直接使用统计学公式计算C^(m-1)_(m+n-2)
        :type m: int
        :type n: int
        :rtype: int
        """
        if m<=1 and n<=1:
            return 1
        c1=m+n-2
        temp=c2=min(m-1,n-1)
        mul1=mul2=1
        while temp>=1:
            mul1=mul1*c1
            c1-=1
            temp-=1
        while c2>=1:
            mul2=mul2*c2
            c2-=1
        return int(mul1/mul2)
#测试代码
t=Solution()
print(t.uniquePaths(3,2))
print(t.uniquePaths(7,3))