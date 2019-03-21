"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-hard/55/array-and-strings/124/
题目：螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]


@author Niefy
@date 2019-03-21
"""
import math
class Solution:
    def spiralOrder(self, matrix):
        if(len(matrix)<1):
            return matrix
        m,n=len(matrix),len(matrix[0]) #行数和列数
        def getCicle(dep):
            if dep>m/2 or dep>n/2:
                return None
            i,j=dep,dep
            res=[matrix[i][j]]#装入起始位置
            while j+1<n-dep:  #向右
                j+=1
                res.append(matrix[i][j])
            while i+1<m-dep:  #向下
                i+=1
                res.append(matrix[i][j])
            while j>dep and dep+1<m-dep:   #向左（有向下走过才需要向左，否则就是原路径返回了）
                j-=1
                res.append(matrix[i][j])
            while i>dep+1 and dep+1<n-dep:   #向上（有向右走过才需要向上）
                i-=1
                res.append(matrix[i][j])
            print("跑圈深度：",dep,'结果：',res)
            return res
        order=[]
        maxDepth=min(math.ceil(m/2),math.ceil(n/2))
        for dep in range(maxDepth):
            order.extend(getCicle(dep))
        return order

        
#测试代码
t=Solution()
a=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
# print(t.spiralOrder(a))

b=[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
# print(t.spiralOrder(b))

c=[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ],
    [ 10,11,12 ]
]
# print(t.spiralOrder(c))

print(t.spiralOrder([]))