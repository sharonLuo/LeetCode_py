"""
Description:

Count the number of prime numbers less than a non-negative number, n.

西元前250年，希腊数学家厄拉多塞(Eeatosthese)想到了一个非常美妙的质数筛法，减少了逐一检查每个数的的步骤，可以比较简单的从一大堆数字之中，筛选出质数来，这方法被称作厄拉多塞筛法(Sieve of Eeatosthese)。

具体操作：先将 2~n 的各个数放入表中，然后在2的上面画一个圆圈，然后划去2的其他倍数；第一个既未画圈又没有被划去的数是3，将它画圈，再划去3的其他倍数；现在既未画圈又没有被划去的第一个数 是5，将它画圈，并划去5的其他倍数……依次类推，一直到所有小于或等于 n 的各数都画了圈或划去为止。这时，表中画了圈的以及未划去的那些数正好就是小于 n 的素数。
其实，当你要画圈的素数的平方大于 n 时，那么后面没有划去的数都是素数，就不用继续判了。
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        else:
            l = [True]*n  ## by default all are primes only change to false if they are not prime (true if it is not a multiple of all previous numbers, then it is a prime)
            l[0] = l[1] = False ### for 0,1, once marked as false
            i = 2 ## we know 2 is prime number, hence 2, 4, 6, 8, ... not prime
            while i * i < n:
                if l[i]:
                    j = i + i
                    while j < n:
                        l[j] = False
                        j += i
                i += 1
            count = 0
            for t in l:
                if t is True:
                    count += 1
            return count
        
        
            
        
        