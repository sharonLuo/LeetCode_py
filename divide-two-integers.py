"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

"""


class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        sum = 0; count = 0; res = 0
        a = abs(dividend); b = abs(divisor)
        if a < b: return 0
        while a >= b:
            sum = b
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count
        if sign == 1:
            return res if res <= MAX_INT else MAX_INT
        if sign == -1:
            return 0-res if res >= MIN_INT else MIN_INT



class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            k = 0; tmp = divisor
            while dividend >= tmp:
                quotient += 1 << k
                dividend -= tmp
                tmp <<= 1
                k += 1
        if sign == 1:
            return quotient if quotient <= MAX_INT else MAX_INT
        if sign == -1:
            return 0-quotient if quotient >= MIN_INT else MIN_INT
