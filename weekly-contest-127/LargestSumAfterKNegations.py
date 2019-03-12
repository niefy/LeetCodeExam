"""
题目：1005. K 次取反后最大化的数组和
给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）
以这种方式修改数组后，返回数组可能的最大和。

示例 1：
输入：A = [4,2,3], K = 1
输出：5
解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。

示例 2：
输入：A = [3,-1,0,2], K = 3
输出：6
解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。

示例 3：
输入：A = [2,-3,-1,5,-4], K = 2
输出：13
解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。
 

提示：
1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100

@author Niefy
@date 2019-03-12
"""
class Solution:
    def largestSumAfterKNegations(self, A, K) -> int:#把数组从小到大排序，如有负数先依次取反，若负数全部取反后还有修改次数未用完，全部用到绝对值最小的那个值上面（一定是最后修改的那个或者下一个）
        A.sort()
        i=0
        absMinIndex=0 #绝对值最小的序号
        while i<K and i<len(A) and A[i]<0:
            A[i]=-A[i]
            absMinIndex=i
            i+=1
        print(A)
        if i<K: #还需K-i次数组修改
            if A[i]<A[absMinIndex]:#绝对值最小除在0前后
                absMinIndex=i
            print("最小绝对值",A[absMinIndex])
            A[absMinIndex]=A[absMinIndex]*(-1)**(K-i)
        return sum(A)

# 测试代码
t=Solution()
A = [4,2,3]
print(t.largestSumAfterKNegations(A,1))
A = [3,-1,0,2]
print(t.largestSumAfterKNegations(A,3))
A = [2,-3,-1,5,-4]
print(t.largestSumAfterKNegations(A,2))
A=[-2,9,9,8,4]
print(t.largestSumAfterKNegations(A,5))