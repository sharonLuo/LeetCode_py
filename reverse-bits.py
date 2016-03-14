"""

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
"""

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        rst = 0
        ttl_digit = 32
        
        while ttl_digit > 0:
            rst = 2 * rst + (n & 1)
            n = n >> 1
            ttl_digit -= 1
            
        return rst
        

"""     
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        rst = 0
        ind_sum = []
        for inx in range(32):
            ind_sum.append(2 ** inx)
        ind_sum.sort(reverse=True)
        
        for inx in range(32):
            rst += ind_sum[inx] * (n & 1)
            n = n >> 1
        return rst
"""     
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        else:
            count = 1
            prime_set = set()
            prime_set.add(2)
            for num in range(3, n, 2):
                if self.is_prime(num, prime_set):
                    count += 1
                    prime_set.add(num)
            return count         
                 
    def is_prime(self, num, prime_set):
        i = 2
        while i in prime_set:
            if num % i == 0:
                return False
            i += 1
        return True
