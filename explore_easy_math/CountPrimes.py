"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/25/math/61/
题目：计数质数
统计所有小于非负整数 n 的质数的数量。

示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""
import math
import time
class Solution:
    def countPrimes(self, n):#列出所有质数
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        primes=[2]
        for k in range(3,n,2):
            isPrime=True#先假设是质数
            for prime in primes:
                if prime*prime>k:#到sqrt(k)后不再判断
                    break
                if k%prime==0:
                    isPrime=False
                    break
            if isPrime:
                primes.append(k)
        print(primes)
        return len(primes)

    def countPrimes1(self, n):#统计非质数个数
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        isPrimes=[True]*(n) #初始先全部设为非质数
        isPrimes[0],isPrimes[1]=False,False #0,1不是质数
        i=2
        while i*i<n:
            if isPrimes[i]: #i为质数，则将i的所有倍数都设为非质数
                j=2*i
                while j<n:
                    isPrimes[j]=False
                    j+=i
            i+=1
        print(isPrimes)
        return isPrimes.count(True)





#测试代码
t=Solution()
print(t.countPrimes1(10))