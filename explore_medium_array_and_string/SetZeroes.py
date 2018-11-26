"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/76/
题目：
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:
输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？

@author Niefy
@date 2018-11-23
"""
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        zerosRow=[]
        zerosCol=[]
        i=0
        while i<len(matrix):
            j=0
            while j<len(matrix[i]):
                if matrix[i][j]==0:
                    zerosRow.append(i)
                    zerosCol.append(j)
                j+=1
            i+=1
        print(zerosCol)
        print(zerosRow)
        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[i]):
                if (i in zerosRow) or (j in zerosCol):
                    matrix[i][j]=0
                j += 1
            i += 1

    def setZeroes1(self, matrix): # LeetCode高分解答
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        idx=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    idx.append((i,j))
        while idx:
            i,j=idx.pop()
            matrix[i]=[0]*n
            for k in matrix:
                k[j]=0

#测试代码
t=Solution()
matrix=[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
t.setZeroes1(matrix)
print(matrix)