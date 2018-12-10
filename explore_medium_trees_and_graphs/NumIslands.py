"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/32/trees-and-graphs/90/
题目：岛屿的个数
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:
输入:
11110
11010
11000
00000

输出: 1

示例 2:
输入:
11000
11000
00100
00011

输出: 3

@author Niefy
@date 2018-12-10
"""

class Solution(object):

    def removeIsland(self,grid,i,j):
        if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]) and grid[i][j]=="1":
            grid[i][j]="0"
            self.removeIsland(grid,i-1,j)
            self.removeIsland(grid,i+1,j)
            self.removeIsland(grid,i,j-1)
            self.removeIsland(grid,i,j+1)

    def numIslands(self, grid):#参考：http://www.cnblogs.com/theskulls/p/4875599.html
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        if n==0:
            return 0
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    self.removeIsland(grid,i,j)
                    count+=1
        return count

        

#测试代码
t=Solution()
grid=[
  ["0", "1", "0", "0", "1"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "0", "1", "1"],
  ["0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "1"]
]
print(t.numIslands(grid))
