"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
"""


import sys
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        q = [1]
        inx_lst = [0]*len(primes)
        while len(q) < n:
            for inx in range(len(inx_lst)):
                while primes[inx]*q[inx_lst[inx]] <= q[-1]:
                    inx_lst[inx] += 1
            min = sys.maxint
            for inx in range(len(inx_lst)):
                if primes[inx]*q[inx_lst[inx]] < min:
                    min = primes[inx]*q[inx_lst[inx]]
            q.append(min)
        return q[-1]
           

### using heap, merge ...            
class Solution(object):
	def nthSuperUglyNumber(self, n, primes):
		uglies = [1]
		def gen(prime):
			for ugly in uglies:
				yield ugly * prime
		merged = heapq.merge(*map(gen, primes))
		while len(uglies) < n:
			ugly = next(merged)
			if ugly != uglies[-1]:
				uglies.append(ugly)
		return uglies[-1]




class Solution(object):
	def nthSuperUglyNumber(self, n, primes):
		uglies = [1]
		merged = heapq.merge(*map(lambda p: (u*p for u in uglies), primes))
		uniqed = (u for u, _ in intertools.groupby(merged))
		map(uglies.append, itertools.islice(unique, n-1))
		return uglies[-1]

		