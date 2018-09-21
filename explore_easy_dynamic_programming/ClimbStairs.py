"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/23/dynamic-programming/54/
题目：爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

@author Niefy
@date 2018-09-21
"""
class ClimbStairs:
    def climbStairs(self, n):#第n级台阶的走法f(n)=f(n-1)+f(n-2)。即最后一步要么走1步，方法数为f(n-1)；要么走2步，方法数为f(n-2)
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        sum=[1,2]
        for x in range(2,n):
            temp=sum[0]
            sum[0]=sum[1]
            sum[1]=temp+sum[0]
        return sum[1]

# 测试代码
t=ClimbStairs()
for x in range(10):
    print(t.climbStairs(x))



