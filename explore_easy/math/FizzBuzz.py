"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/25/math/60/
题目：写一个程序，输出从 1 到 n 数字的字符串表示。
1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：
n = 15,
返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

@author Niefy
@date 2018-11-20
"""
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        array=[]
        i=1
        while i<=n:
            if i%15==0:
                array.append("FizzBuzz")
            elif i%5==0:
                array.append("Buzz")
            elif i%3==0:
                array.append("Fizz")
            else:
                array.append(str(i))
            i+=1
        return array
#测试用例
t=Solution()
print(t.fizzBuzz(15))