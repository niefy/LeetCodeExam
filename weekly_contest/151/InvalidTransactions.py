"""
https://leetcode-cn.com/contest/weekly-contest-151/problems/invalid-transactions/
题目. 查询无效交易 

如果出现下述两种情况，交易 可能无效：

1.交易金额超过 ¥1000
2.或者，它和另一个城市中同名的另一笔交易相隔不超过 60 分钟（包含 60 分钟整）
每个交易字符串 transactions[i] 由一些用逗号分隔的值组成，这些值分别表示交易的名称，时间（以分钟计），金额以及城市。

给你一份交易清单 transactions，返回可能无效的交易列表。你可以按任何顺序返回答案。

 

示例 1：
输入：transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
输出：["alice,20,800,mtv","alice,50,100,beijing"]
解释：第一笔交易是无效的，因为第二笔交易和它间隔不超过 60 分钟、名称相同且发生在不同的城市。同样，第二笔交易也是无效的。

示例 2：
输入：transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
输出：["alice,50,1200,mtv"]

示例 3：
输入：transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
输出：["bob,50,1200,mtv"]
 

提示：

1.transactions.length <= 1000
2.每笔交易 transactions[i] 按 "{name},{time},{amount},{city}" 的格式进行记录
3.每个交易名称 {name} 和城市 {city} 都由小写英文字母组成，长度在 1 到 10 之间
4.每个交易时间 {time} 由一些数字组成，表示一个 0 到 1000 之间的整数
5.每笔交易金额 {amount} 由一些数字组成，表示一个 0 到 2000 之间的整数

@author Niefy
@date 2019-08-30
"""
class Solution:
    def invalidTransactions(self, transactions):
        dict={}
        for i in range(len(transactions)):#数据格式整理
            transaction=transactions[i]
            [name,time,amount,city]=transaction.split(',')
            if not(name in dict):
                dict[name]=[]
            dict[name].append([int(time),int(amount),city,False,i])
        # print(dict)
        res=[]
        for name in dict:
            nameTrans=dict[name]
            length = len(nameTrans)
            for i in range(0,length):
                if nameTrans[i][1]>1000 and not(nameTrans[i][3]):
                    nameTrans[i][3]=True
                    res.append(transactions[nameTrans[i][4]])
                for j in range(i+1,length):
                    if(nameTrans[i][2]!=nameTrans[j][2] and abs(nameTrans[i][0]-nameTrans[j][0])<=60):
                        if not(nameTrans[i][3]):
                            nameTrans[i][3]=True
                            res.append(transactions[nameTrans[i][4]])
                        if not(nameTrans[j][3]):
                            nameTrans[j][3]=True
                            res.append(transactions[nameTrans[j][4]])
        return res

# 测试用例
t=Solution()
# print(t.invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"]))

# print(t.invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]))

# print(t.invalidTransactions(["alice,20,800,mtv","bob,50,1200,mtv"]))

print(t.invalidTransactions(["bob,627,1973,amsterdam","alex,387,885,bangkok","alex,355,1029,barcelona","alex,587,402,bangkok","chalicefy,973,830,barcelona","alex,932,86,bangkok","bob,188,989,amsterdam"]))