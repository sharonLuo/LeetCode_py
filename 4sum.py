"""
Given an array S of n integers, are there elements a, b, c, d in S such that a + b + c + d= target? Find all unique tuples in the array which gives the sum of target.

Note:
Elements in a tuple (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate tuples.
    For example, given array S = {-4 -3 -3 -3 -2 0 0 3 5 8},

    A solution set is:
    (-4, -3, 0, 8)
    (-4, -3, 3, 5)
    (-4,  0, 0, 5)
    (-2,  0, 0, 3)
 """   

"""
Trade space with time. first iterate the num and use 2 sum as the key, indexes as the value in hash table.
Then we start iterate again. take target -num[i]-num[j]，if it is still in the hashtable, we take out the values and make the solution. 
The overall time and space complexity are both O(n^2)
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        size, rst, d = len(nums), [], {}
        if size < 4:
            return rst
        nums.sort()
        for p in range(size):
            for q in range(p+1, size):
                if nums[p] + nums[q] not in d:
                    d[nums[p]+nums[q]] = [(p,q)]
                else:
                    d[nums[p]+nums[q]].append((p,q))
        
        for i in range(size):
            for j in range(i+1, size-2):
                T = target-nums[i]-nums[j]
                if T in d:
                    for k in d[T]:
                        if k[0] > j and [nums[i], nums[j], nums[k[0]], nums[k[1]]] not in rst: 
                            rst.append([nums[i], nums[j], nums[k[0]], nums[k[1]]])
        return rst



###  Solution might ETL on Leetcode
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        rst = []
        for m in range(len(nums)-3):
            if m > 0 and nums[m-1] == nums[m]:
                continue
            for i in range(m+1, len(nums)-2):
                if nums[i-1] == nums[i] and i-m >1:
                    continue
                j, k = i+1, len(nums)-1
                while j < k :
                    if nums[j] + nums[k] < target-nums[i]-nums[m]:
                        j += 1
                    elif nums[j] + nums[k] > target-nums[i]-nums[m]:
                        k -= 1
                    else:
                        rst.append([nums[m], nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                        while j < k and nums[k] == nums[k+1]:
                            k -= 1
        return rst


