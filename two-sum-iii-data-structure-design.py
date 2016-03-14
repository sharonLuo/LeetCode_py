"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
"""


### 580 ms
class TwoSum:

    def __init__(self):
        self.ctr = {}

    def add(self, number):
        if number in self.ctr:
            self.ctr[number] += 1
        else:
            self.ctr[number] = 1

    def find(self, value):
        ctr = self.ctr
        for num in ctr:
            if value - num in ctr and (value - num != num or ctr[num] > 1):
                return True
        return False
        


##### 870 ms
class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.nums = {}
        self.sum = set()
        

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.nums[number] = self.nums.get(number, 0) + 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if value in self.sum:
            return True
        for num in self.nums:
            if value-num==num:
                if self.nums[num]>1:
                    self.sum.add(value)
                    return True
            else:
                if value-num in self.nums:
                    self.sum.add(value)
                    return True
        return False
                
        

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
