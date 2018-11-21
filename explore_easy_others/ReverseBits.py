"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/26/others/66/
题目：颠倒给定的 32 位无符号整数的二进制位。

示例:
输入: 43261596
输出: 964176192
解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
     返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。
进阶:
如果多次调用这个函数，你将如何优化你的算法？
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s1=str(bin(n))
        print('转二进制：',s1)
        s2=s1[:1:-1]
        print('颠倒:',s2)
        while len(s2)<32:
            s2=s2+'0'
        print('补0后:', s2)
        int4=int(s2,2)
        return int4

print(int("00111001011110000010100101000000",2))
t=Solution()
print(t.reverseBits(43261596))