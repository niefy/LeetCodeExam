"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/26/others/65/
题目：两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:
输入: x = 1, y = 4
输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        s1=str(bin(x))[:1:-1] #去除前面的0b，并倒序
        print('s1=',s1)
        s2=str(bin(y))[:1:-1]
        print('s2=',s2)
        i=0
        minLen=min(len(s1),len(s2))
        count=0
        while i<minLen:
            if s1[i]!=s2[i]:
                count+=1
            i+=1
        return count+s1[minLen:].count('1')+s2[minLen:].count('1')

t=Solution()
print(t.hammingDistance(1,4))