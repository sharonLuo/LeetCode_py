
"""
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example: 
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
"""

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dict = {}
        for word in dictionary:
            abbr = self.computeAbbr(word)
            #self.dict[abbr] = self.dict.get(abbr, set())
            self.dict[abbr] = self.dict.get(abbr, [])
            self.dict[abbr].add(word)
        return
        

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.computeAbbr(word)
        if not abbr in self.dict:
            return True
        if word in self.dict[abbr]:
            return len(self.dict[abbr])==1
        return False
        
    def computeAbbr(self, word):
        if len(word)<=2:
            return word
        else:
            return word[0]+str(len(word)-2)+word[-1]
        



