"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/31/
题目：旋转图像
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。

说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

@author Niefy
@date 2018-09-12
"""
class RotateImage:
    def rotate(self, matrix):#解答来自 https://blog.csdn.net/shawpan/article/details/69663710
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:]=map(list,zip(*matrix[::-1]))

# 测试代码
t=RotateImage()
matrix=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
t.rotate(matrix)
print(matrix)