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
from sys import maxsize
import math
class Solution:
    def coinChange(self, coins, amount):#动态规划，参考https://www.cnblogs.com/hapjin/p/5578852.html
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        len_coins=len(coins)
        c=[[0]*(amount+1)]*(len_coins+1)
        c[0]=[maxsize]*(amount+1)
        for j_money in range(1,amount+1): #j_money为要找零的金额
            for i_coin in range(1,len_coins+1):
                if j_money<coins[i_coin-1]:
                    c[i_coin][j_money] = c[i_coin-1][j_money]
                    continue
                c[i_coin][j_money]=min(c[i_coin-1][j_money],c[i_coin][j_money-coins[i_coin-1]]+1)
        return c[len_coins][amount] if c[len_coins][amount]<maxsize else -1
    

    def coinChange1(self, coins, amount):#来源，LeetCode高分解答https://leetcode-cn.com/submissions/detail/11529150/
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        ll,result = len(coins),amount+1
        
        def countCoins(index,target,count):
            nonlocal result
            if count + math.ceil(target/coins[index]) >= result:
                return
            
            if target%coins[index] == 0:
                result = count + target//coins[index]
                return
            
            if index == ll-1:
                return
            
            for i in range(target//coins[index],-1,-1):
                countCoins(index+1,target-coins[index]*i,count+i)
                
        countCoins(0,amount,0)
        return -1 if result > amount else result

# 测试代码
t=Solution()
# print(t.coinChange([1,3,4],6))
# print(t.coinChange([3,5],7))

print(t.coinChange1([1,3,4],6))