"""
Ugly Number II My Submissions Question
Total Accepted: 17646 Total Submissions: 71946 Difficulty: Medium
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Hint:

The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = [1]
        i2 = i3 = i5 = 0
        while len(q) < n:
            while q[i2]*2 <= q[-1]: 
                i2 += 1
            while q[i3]*3 <= q[-1]:
                i3 += 1
            while q[i5]*5 <= q[-1]:
                i5 += 1
            q.append(min(2*q[i2], 3*q[i3], 5*q[i5]))
        return q[-1]
        


###### WRONG, doesn't account for 2*3 and 3*2 for repetition
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = [1]
        i2 = i3 = i5 = 0
        while len(q) < n:
            m2, m3, m5 = q[i2]*2, q[i3]*3, q[i5]*5
            m = min(m2,m3,m5)
            if m == m2:
                i2 += 1
            elif m == m3:
                i3 += 1
            else:
                i5 += 1
            q.append(m)
        return q[-1]
        
