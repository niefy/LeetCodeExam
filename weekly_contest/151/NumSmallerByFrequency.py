"""
https://leetcode-cn.com/contest/weekly-contest-151/problems/compare-strings-by-frequency-of-the-smallest-character/
题目：比较字符串最小字母出现频次  显示英文描述  
用户通过次数 485
用户尝试次数 533
通过次数 492
提交次数 892
题目难度 Easy
我们来定义一个函数 f(s)，其中传入参数 s 是一个非空字符串；该函数的功能是统计 s  中（按字典序比较）最小字母的出现频次。

例如，若 s = "dcce"，那么 f(s) = 2，因为最小的字母是 "c"，它出现了 2 次。

现在，给你两个字符串数组待查表 queries 和词汇表 words，请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是满足 f(queries[i]) < f(W) 的词的数目，W 是词汇表 words 中的词。

 

示例 1：
输入：queries = ["cbd"], words = ["zaaaz"]
输出：[1]
解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。

示例 2：
输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
输出：[1,2]
解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
 

提示：

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] 都是小写英文字母

@author Niefy
@date 2019-08-30
"""
class Solution:
    def numSmallerByFrequency(self, queries, words):
        res=[0]*len(queries)
        fw=[0]*len(words)
        for i in range(0,len(words)):
            fw[i]=self.f(words[i])
        fw.sort()
        print("fw=",fw)
        for i in range(0,len(queries)):
            fqi=self.f(queries[i])
            for fwi in fw:
                if(fqi<fwi):
                    res[i]+=1
        return res

    def f(self, str):#函数f(s)
        min=str[0]
        count=0
        for s in str:
            if s<min:
                min=s
                count=1
            elif s==min:
                count+=1
        return count
#测试用例
t=Solution()
# print(t.f("zaaaz"),t.f("aabbbcccc"))
print(t.numSmallerByFrequency(["cbd"],["zaaaz"]))
print(t.numSmallerByFrequency(["bbb","cc"],["a","aa","aaa","aaaa"]))