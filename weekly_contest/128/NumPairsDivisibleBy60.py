"""
https://leetcode-cn.com/contest/weekly-contest-128/problems/pairs-of-songs-with-total-durations-divisible-by-60/
题目：1013. 总持续时间可被 60 整除的歌曲
在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。

返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字  i < j 且有 (time[i] + time[j]) % 60 == 0。

 

示例 1：

输入：[30,20,150,100,40]
输出：3
解释：这三对的总持续时间可被 60 整数：
(time[0] = 30, time[2] = 150): 总持续时间 180
(time[1] = 20, time[3] = 100): 总持续时间 120
(time[1] = 20, time[4] = 40): 总持续时间 60
示例 2：

输入：[60,60,60]
输出：3
解释：所有三对的总持续时间都是 120，可以被 60 整数。
 

提示：

1 <= time.length <= 60000
1 <= time[i] <= 500


@author Niefy
@date 2019-03-18
"""
class Solution:
    def numPairsDivisibleBy60(self, time) -> int: #两两计算方式，超出时间限制
        length=len(time)
        count=0
        for i in range(0,length):
            for j in range(i+1,length):
                if (time[i]+time[j])%60==0:
                    count+=1
        return count

    def numPairsDivisibleBy60_1(self, time) -> int: #全部除以60，将余数分为等于0、小于30、等于30、大于30 的3组
        r1,r2=[],[] #分别为小于30的余数和大于30的余数
        countR0,countR30=0,0 #余数等于30的个数
        for i in range(0,len(time)):
            remain=time[i]%60
            if(remain==0):
                countR0+=1
            elif(remain<30):
                r1.append(remain)
            elif(remain==30):
                countR30+=1
            else:
                r2.append(remain)
        count=0
        if(countR0>1): #n选2
            count+=countR0*(countR0-1)/2
        if(countR30>1):#n选2
            count+=countR30*(countR30-1)/2
        for i in range(len(r1)):
            for j in range(len(r2)):
                if r1[i]+r2[j]==60:
                    count+=1
        return int(count)
        

#测试代码
t=Solution()
print(t.numPairsDivisibleBy60_1([30,20,150,100,40]))
print(t.numPairsDivisibleBy60_1([60,60,60]))