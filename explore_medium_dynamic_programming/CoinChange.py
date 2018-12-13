"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/51/dynamic-programming/106/
题目：零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1

示例 2:
输入: coins = [2], amount = 3
输出: -1

说明:
你可以认为每种硬币的数量是无限的。

@author Niefy
@date 2018-12-13
"""
class Solution:
    def coinChange(self, coins, amount):#leetcode提交超时
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        print(coins)
        def reduce(num):
            for coin in coins:
                if num%coin==0:
                    print('%d*%d'%(coin,int(num/coin)),end=',')
                    return int(num/coin)
                if coin>num:
                    continue
                remain=reduce(num-coin)
                if remain<0:
                    continue
                else:
                    print(coin,end=',')
                    return  1+remain
            return -1   
        return reduce(amount)



# 测试代码
t=Solution()
print(t.coinChange([1,2, 5],13))