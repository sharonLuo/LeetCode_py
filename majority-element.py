class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ###### since majority element appears more than floor(n/2) times, the middle element must be it
        
        # list, slow
        #nums.sort()
        #m = len(nums)/2
        #return nums[m]
        
        # dictionary, fast
        d = {}
        m = len(nums)/2
        for k in nums:
            if k not in d:
                d[k] = 1
            else:
                d[k] += 1
        for k in nums:
            if d[k] > m:
                return k
        
        