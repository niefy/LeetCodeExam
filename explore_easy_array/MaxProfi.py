"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/22/
题目：买卖股票的最佳时机 II
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例 3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

@author Nifury
@date 2018-09-11
"""


class MaxProfit:
    # 策略：跌前卖出（如有持仓），正在上涨则无需操作
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0  # 下标，代表第几天
        lastIndex = len(prices) - 1  # 最后一天的下标
        hasPosition = False  # 是否有持仓
        positionBuyPrice = None  # 持仓买入价格
        totalProfit = 0  # 利润
        while i < len(prices):
            if i < lastIndex and hasPosition == False and prices[i + 1] > prices[i]:  # 无持仓、要上涨，应该买入(如为最后一天则不再买入)
                positionBuyPrice = prices[i]
                print('买入，当前价格：', positionBuyPrice)
                hasPosition = True
            elif hasPosition and (i == lastIndex or prices[i + 1] < prices[i]):  # 有持仓、要下跌，应该卖出(如为最后一天且还有持仓也卖出)
                profit = prices[i] - positionBuyPrice  # 本次收益
                print('卖出，当前价格：', prices[i], ',本次获得收益：', profit)
                totalProfit += profit
                hasPosition = False
            i += 1
        return totalProfit


# 测试代码
t = MaxProfit()
profit = t.maxProfit([7, 1, 5, 3, 6, 4])
print('总收益：', profit)
