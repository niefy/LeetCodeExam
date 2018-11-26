"""
https://leetcode-cn.com/contest/weekly-contest-85/problems/rectangle-overlap/
题目：836. 矩形重叠

矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。

如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。

给出两个矩形，判断它们是否重叠并返回结果。

示例 1：

输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
输出：true
示例 2：

输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
输出：false
说明：

两个矩形 rec1 和 rec2 都以含有四个整数的列表的形式给出。
矩形中的所有坐标都处于 -10^9 和 10^9 之间。

@author Niefy
@date 2018-11-23
"""
class Solution:
    def isInRect(self,m,n,rect):#判断点(m,n)是否在矩阵rect内
        x1, y1, x2, y2 = rect
        return m>x1 and m<x2 and n>y1 and n<y2

    def isRectangleOverlap(self, rec1, rec2):#运行结果不正确
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2=rec1
        m1,n1,m2,n2=rec2
        if x1==m1 and y1==n1 and x2==m2 and y2==n2:#完全重叠
            return True
        points1 = [(x1, y1), (x2, y2), (x1, y2), (x2, y1)]  # 四个顶点坐标
        while points1:#判断rect1的四个顶点坐标是否在rect2内
            x,y=points1.pop()
            if self.isInRect(x,y,rec2):
                return True
        points2 = [(m1, n1), (m2, n2), (m1, n2), (m2, n1)]
        while points2:#判断rect2的四个顶点坐标是否在rect1内
            m,n=points2.pop()
            if self.isInRect(m,n,rec1):
                return True
        return False

    def isRectangleOverlap1(self, rec1, rec2):#如果两个矩形重叠，那么其中一个矩形至少有一个顶点在另一矩形内
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        minx1, miny1, maxx1, maxy1 = rec1
        minx2, miny2, maxx2, maxy2 = rec2
        minx = max(minx1, minx2)
        miny = max(miny1, miny2)
        maxx = min(maxx1, maxx2)
        maxy = min(maxy1, maxy2)
        print(minx, miny, maxx, maxy)
        if minx > maxx:
            return False
        if miny > maxy:
            return False
        if (maxx - minx) * (maxy - miny) > 0:
            return True
        return False

#测试代码
t=Solution()
print(t.isRectangleOverlap(rec1 = [0,0,2,2], rec2 = [1,1,3,3]))
print(t.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [1,0,2,1]))
print(t.isRectangleOverlap([7,8,13,15],[10,8,12,20]))