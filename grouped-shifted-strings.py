"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
Note: For the return value, each inner list's elements must follow the lexicographic order.
"""


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        mp = {}
        for ele in strings:
            value = self.getShiftPattern(ele)
            mp[value] = mp.get(value, [])
            mp[value].append(ele)
        rst = [sorted(mp[key]) for key in mp]
        return rst

    def getShiftPattern(self, word):
        size = len(word)
        # this can be omitted since range(1,1) won't through out error
        #if size < 2:
        #    return "0"
        rst = ""
        for inx in range(1,size):
            tmp = ord(word[inx])-ord(word[0])
            if tmp < 0:
                tmp = tmp + 26
            rst = rst + str(tmp) + "*"
        return rst

 