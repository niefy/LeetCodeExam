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

@author Niefy
@date 2018-12-12
"""
class Solution(object):
    def isEffectParentesis(self,str):
        """
        判断括号组合是否有效
        """
        countLeft=0
        for k in str:
            if k=='(':
                countLeft+=1
            else:
                countLeft-=1
            if countLeft<0:
                return False
        return countLeft==0

    def generateParenthesis(self, n):
        """
        如n=3时，假设有1-6的6个位置，从中任选3个位置来放左括号，其余位置放右括号，剔除无效的组合后即为最终结果
        :type n: int
        :rtype: List[str]
        """
        if n<1:
            return []
        result=[]
        def append(str,leftRemain,rightRemain):
            if rightRemain>0 and rightRemain>=leftRemain:#右括号数量还有剩余(剩余右括号比剩余左括号少无效)
                if leftRemain>0:
                    append(str+'(',leftRemain-1,rightRemain)
                    append(str+')',leftRemain,rightRemain-1)
                else:
                    append(str+')',leftRemain,rightRemain-1)
            elif leftRemain==0:#左右大括号刚好全用掉
                result.append(str)
        append('(',n-1,n)
        return result

        


# 测试代码
t=Solution()
print(t.generateParenthesis(4))
