"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/23/dynamic-programming/55/
题目：买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。

@author Niefy
@date 2018-09-25
"""
class MaxProfit:
    def maxProfit(self, prices):#依次遍历，记录之前的最小股价和最大收益，遍历每项检查是否可能超过最大收益
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <= 1:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for x in prices:
            if x <= minPrice:
                minPrice = x
            else:
                maxProfit = max(maxProfit, x - minPrice)
        return maxProfit

#测试代码
t=MaxProfit()
print(t.maxProfit([7,1,5,3,6,4]))