"""
There are two sorted arrays nums1 and nums2 of size m and n respectively. 
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        total = m + n
        if total%2 == 0:  ### even total
            return (self.findKthSortedArrays(nums1, m, nums2, n, total/2) + self.findKthSortedArrays(nums1, m, nums2, n, total/2+1))/2.0
        else:
            return self.findKthSortedArrays(nums1, m, nums2, n, (total+1)/2)
        
    def findKthSortedArrays(self, nums1, m, nums2, n, k):
        # always assume m <= n
        if m > n:
            return self.findKthSortedArrays(nums2, n, nums1, m, k)
        if m == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        
        # divide k into two parts
        ia = min(k/2, m)
        ib = k-ia
        if nums1[ia-1] < nums2[ib-1]:
            return self.findKthSortedArrays(nums1[ia:], m-ia, nums2, n, k-ia)
        elif nums1[ia-1] > nums2[ib-1]:
            return self.findKthSortedArrays(nums1, m, nums2[ib:], n-ib, k-ib)
        else:
            return nums1[ia-1]
    
  
