"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
"""

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        numDict = collections.OrderedDict()
        for x in range(len(nums)):
            key = nums[x] / max(1, t)
            for m in (key, key - 1, key + 1):
                if m in numDict and abs(nums[x] - numDict[m]) <= t:
                    return True
            numDict[key] = nums[x]
            if x >=  k:
                numDict.popitem(last=False)
        return False




class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        pp = sorted(zip(nums, range(len(nums))), key= lambda x:x[0])
        return self.search(pp,t ,k )
      
    def search(self, l, t, k):
        po = 0
        while po < len(l):
            i = po + 1
            while i < len(l):
                if abs(l[i][0] - l[po][0]) <= t and abs(l[i][1] - l[po][1]) <= k:
                    return True
                else:
                    if abs(l[i][0] - l[po][0]) > t:
                        break
                    else:
                        i +=1
            po += 1
        return False    
         
