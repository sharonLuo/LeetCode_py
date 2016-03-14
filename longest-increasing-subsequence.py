"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""



##### O(n log n)
"""
dp 维护一个递增的subsequence, 它的长度仅当找到一个满足条件的递增元素才会增加
且dp[low]=nums[x], 新替换的dp[low]元素只会比原来在这个位置上的元素要小, 所以后面增加的dp部分可以加在原的基础上, dp的长度为最终所求
例如[1,5,7,2,3,4,8]
dp的变化为
[] -> [1] -> [1,5] -> [1,5,7] -> [1,2,7] -> [1,2,3] -> [1,2,3,4] -> [1,2,3,4,8]
可以看到dp并不总是满足条件的subsequence, 但长度都是对的
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) / 2
                if dp[mid] >= nums[x]:
                    high = mid - 1
                else:
                    low = mid + 1
            ### low的值为nums[x]应该出现在的位置
            if low >= len(dp):
                dp.append(nums[x]) ###仅当满足条件才会增加dp的长度
            else:
                dp[low] = nums[x]
        return len(dp)

### O(n^2)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = [1]*size
        for i in range(size):
        	for j in range(i):
        		if nums[j] < nums[i]:
        			dp[i] = max(dp[i], dp[j]+1)
胡想001
        return max(dp) if dp else 0

