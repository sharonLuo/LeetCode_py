"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

## beat 67%
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        length_a = len(a)
        length_b = len(b)
        max_length = max(length_a, length_b)
        rst = ""
        for inx in range(-1, -1*(max_length+1), -1):
            val = carry
            if -inx <= length_a:
                val += int(a[inx])
            if -inx <= length_b:
                val += int(b[inx])
            carry = val / 2
            rst += str(val % 2)
        if carry == 1:
            rst += str(1)
        new_rst = rst[::-1]
        return new_rst
 