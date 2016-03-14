"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        rst = 0
        for ele in digits:
            rst = 10 * rst + ele
        rst += 1
        new_digits = []
        while rst:
            new_digits.append(rst % 10)
            rst /= 10
        new_digits.reverse()
        return new_digits


class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        flag = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + flag == 10:
                digits[i] = 0
                flag = 1
            else:
                digits[i] = digits[i] + flag
                flag = 0
                break
        
        if flag == 1:
            digits.insert(0, 1)
        return digits        