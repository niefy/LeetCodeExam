"""
https://leetcode-cn.com/contest/weekly-contest-128/problems/capacity-to-ship-packages-within-d-days/
题目：1014. 在 D 天内送达包裹的能力
传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

示例 1：
输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 

示例 2：
输入：weights = [3,2,2,4,1,4], D = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4

示例 3：
输入：weights = [1,2,3,1,1], D = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1

提示：
1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500

@author Niefy
@date 2019-03-20
"""
import math

class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        def tryShip(tryW): #以tryW运载量尝试，检查是否可以在D天内运送
            i,days,tempSum=0,1,0
            while i<len(weights):
                if tempSum+weights[i]<=tryW:#可以装到当天运
                    tempSum+=weights[i]
                else:#超出容量，第二天再运
                    days+=1
                    tempSum=weights[i]
                i+=1
            print('尝试：',tryW,',需要天数：',days)
            return days<=D  #可在D天内运完，则此运载量符合要求
        
        shipMax=sum(weights) #初始尝试最大载重
        shipMin=max(max(weights),math.ceil(shipMax/D)) #初始尝试最小载重
        while True: #通过二分查找找到最小符合要求的载重
            tryW=(shipMin+shipMax)//2 #折半取整
            print(shipMin,'-',shipMax)
            if tryShip(tryW):#能符合则减小再尝试
                if tryW==shipMin:
                    return tryW
                shipMax=tryW
            else:
                if shipMin+1==shipMax:
                    return shipMax
                shipMin=tryW
            
        return None

# 测试代码
t=Solution()
# print(t.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))
# print(t.shipWithinDays([3,2,2,4,1,4],3))
print(t.shipWithinDays([1,2,3,1,1],4))