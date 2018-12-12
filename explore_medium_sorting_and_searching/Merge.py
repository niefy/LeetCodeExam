"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/50/sorting-and-searching/101/
题目：合并区间
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。


@author Niefy
@date 2018-12-12
"""
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
    def __str__(self):
        return '[%s,%s]'%(self.start,self.end)

class Solution:
    def isOverlap(self,interval1,interval2):
        """
        检测两个区间是否重叠
        """
        if interval1.start>interval2.end or interval2.start>interval1.end:
            return False
        return True

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        m=0
        while m<len(intervals):
            n=m+1
            changed=False
            while n<len(intervals):
                if self.isOverlap(intervals[m],intervals[n]):
                    intervals[m].start=min(intervals[m].start,intervals[n].start)
                    intervals[m].end=max(intervals[m].end,intervals[n].end)
                    del intervals[n]
                    changed=True
                else:
                    n+=1
            if not changed:
                m+=1
        return intervals


#测试代码
t=Solution()
intervals=t.merge([Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)])
for item in intervals:
    print(item,end=',')

print()
intervals=t.merge([Interval(1,4),Interval(4,5)])
for item in intervals:
    print(item,end=',')

print()
intervals=t.merge([Interval(2,3),Interval(4,5),Interval(6,7),Interval(8,9),Interval(1,10)])
for item in intervals:
    print(item,end=',')