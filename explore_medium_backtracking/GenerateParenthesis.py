"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/49/backtracking/92/
题目：生成括号
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

n=4，生成结果为：[
    "(((())))",
    "((()()))",
    "((())())",
    "((()))()",
    "(()(()))",
    "(()()())",
    "(()())()",
    "(())(())",
    "(())()()",
    "()((()))",
    "()(()())",
    "()(())()",
    "()()(())",
    "()()()()"
    ]

@author Niefy
@date 2018-12-11
"""
class Solution(object):
    def generateParenthesis(self, n):#每次加多一个括号时，有几种情况（1：加左边 2：加右边 3：左右半边加到外边）
        """
        :type n: int
        :rtype: List[str]
        """
        if n<1:
            return []
        set1={"()"}
        i=1
        while i<n:
            set2=set()
            for item in set1:
                set2.add("()"+item)
                set2.add(item+"()")
                set2.add("("+item+")")
            set1=set2
            i+=1
        return list(set1)


# 测试代码
t=Solution()
print(t.generateParenthesis(4))
