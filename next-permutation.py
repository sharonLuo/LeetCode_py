"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

time O(n), space O(1)
"""

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        n = len(num)
        k = -1
        l = -1
        # Find the largest k such that num[k] < num[k + 1]
        for i in range(n - 1):
            if num[i] < num[i + 1]:
                k = i

        # Find the largest l such that num[k] < num[l] (if k exists)
        if k >= 0:
            for i in range(n):
                if num[i] > num[k]:
                    l = i
            # Swap num[l] and num[k]
            num[l], num[k] = num[k], num[l]

        # Reverse num[k + 1:]
        left = k + 1
        right = n - 1
        while left < right:
            num[left], num[right] = num[right], num[left]
            left += 1
            right -= 1
        
