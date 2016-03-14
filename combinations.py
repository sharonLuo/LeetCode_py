"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

"""
递归解法: 类似permutation
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.dfs(range(1, n+1), k)
    
    def dfs(self, pool, k):
        res = []
        length = len(pool)
        if k <= 0 or length < k:
            return res
        for i in range(length):
            if k == 1:
                res.append([pool[i]])
            else:
                for item in self.dfs(pool[i+1:], k-1):
                    res.append([pool[i]] + item)
        return res

"""
非递归解法p指针指的位置如果达到了允许的最大值, p指针就前移. 
比如c(5,3)得到了[1,2,5], p指针指向第三个位置已经达到了最大值5, 则p前移, 
指向第二个位置, c[p]+= 1, 于是得到[1,3,4]. 当p指向第一个位置且它达到最大值, 也就是[3,4,5]的时候就结束了. 
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if k == 0:
            return res
        c = [0 for i in range(k)]
        p = 0
        ### p is a position, if c[p] reaches max, --p
        while p >= 0:
            c[p] += 1
            for i in range(p+1, k):
                c[i] = c[i-1]+1
            res.append(list(c)) ### finish picking up k numbers
            p = k-1
            while p >= 0 and c[p] == n-(k-1-p): ## 当p指向的位置达到最大(因为c[k-1]=n此时, 则p往前移来permute
                p -= 1
        return res
         




#####################################################            

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.rst = []
        self.count = 0
        self.dfs(n, k, 1,[])
        return self.rst
    
    def dfs(self, n, k, start, valuelist):
        if self.count == k:
            self.rst.append(valuelist)
            return
        for i in range(start, n+1):
            self.count += 1
            self.dfs(n, k, i+1, valuelist+[i])
            self.count -= 1
#####################################################            
    


######## Time Limit Exceed
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0: return []
        if k == 1: return [[w] for w in range(1, n+1)]
        rst = []
        for i in range(1, n+1):
            for j in self.combinePool(range(i+1,n+1), k-1):
                rst.append([i] + j)
        return rst
    
    def combinePool(self, pool, k):
        if k == 0: return []
        if k == 1: return [[w] for w in pool]
        rst = []
        for inx in range(len(pool)):
            for j in self.combinePool(pool[:inx]+pool[inx+1:], k-1):
                rst.append([pool[inx]] + j)
        return rst

    
    