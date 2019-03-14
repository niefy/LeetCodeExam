"""
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/49/backtracking/91/
题目：  电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png


示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

@author Niefy
@date 2018-12-11
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)<1:
            return []
        dict={
            "2":set("abc"),
            "3":set("def"),
            "4":set("ghi"),
            "5":set("jkl"),
            "6":set("mno"),
            "7":set("pqrs"),
            "8":set("tuv"),
            "9":set("wxyz"),
        }
        result=list(dict[digits[0]])
        for number in digits[1:]:
            tempResult=[]
            for char1 in result:
                for char2 in dict[number]:
                    tempResult.append(char1+char2)
            result=tempResult
        return result
            


# 测试代码
t=Solution()
print(t.letterCombinations("342"))
