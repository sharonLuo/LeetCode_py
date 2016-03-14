"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.


"""

class Solution:
    """
    def checkCover(self, dictS, dictT):
        for ele in dictT:
            if ele not in dictS or dictS[ele] < dictT[ele]:
                return False
        return True
    """
    # @return a string
    def minWindow(self, S, T):
        countT={}; countS={}
        for char in T:
            if char not in countT: countT[char]=1
            else: countT[char]+=1
        for char in T:
            if char not in countS: countS[char]=1
            else: countS[char]+=1
            
        start, end = 0, 0
        minstart, minlength, count = 0, len(S), len(T)
        while end < len(S) and start <= end:
            if S[end] in countT:
                countS[S[end]] -= 1
                if countS[S[end]] >= 0:
                    count -= 1
                if count == 0:
                    while True:
                        ### 当发现move forward "start" 会导致不cover T时, stop 以此保证一直cover T, 顾不用改变count的值
                        ### 并且可以根据count的值是否为0, 来判断S中是否有substring cover T
                        if S[start] in countT and countS[S[start]] == 0:
                            break
                        elif S[start] in countT and countS[S[start]] < 0:
                            countS[S[start]] += 1
                        start += 1
                    tmp = end-start+1
                    if tmp < minlength:
                        minstart, minlength = start, tmp
            end += 1
        return "" if count != 0 else S[minstart:(minstart+minlength)]
                


### use match to denote whether there is a substring in S covering T, 0 for False, 1 for True
### use count to denote whether the substring covers T
class Solution:
    """
    def checkCover(self, dictS, dictT):
        for ele in dictT:
            if ele not in dictS or dictS[ele] < dictT[ele]:
                return False
        return True
    """
    # @return a string
    def minWindow(self, S, T):
        countT={}; countS={}
        for char in T:
            if char not in countT: countT[char]=1
            else: countT[char]+=1
        for char in T:
            if char not in countS: countS[char]=1
            else: countS[char]+=1
            
        start, end = 0, 0
        minstart, minlength = 0, len(S)
        match, count = 0, len(T)
        
        while end < len(S) and start <= end:
            if S[end] not in countT:
                end += 1
                continue
            else:
                countS[S[end]] -= 1
                if countS[S[end]] >= 0:
                    count -= 1
                while count == 0:
                    match = 1
                    while S[start] not in countT:
                        start += 1
                    tmp = end-start+1
                    if tmp < minlength:
                        minstart, minlength = start, tmp
                    countS[S[start]] += 1
                    if countS[S[start]] > 0:
                        count += 1
                    start += 1
            end += 1
        return "" if match == 0 else S[minstart:(minstart+minlength)]
                
         
##### Same
class Solution:
    """
    def checkCover(self, dictS, dictT):
        for ele in dictT:
            if ele not in dictS or dictS[ele] < dictT[ele]:
                return False
        return True
    """
    # @return a string
    def minWindow(self, S, T):
        countT={}; countS={}
        for char in T:
            if char not in countT: countT[char]=1
            else: countT[char]+=1
        for char in T:
            if char not in countS: countS[char]=1
            else: countS[char]+=1
            
        start, end = 0, 0
        minstart, minlength = 0, len(S)
        match, count = 0, len(T)
        
        while end < len(S) and start <= end:
            if S[end] in countT:
                countS[S[end]] -= 1
                if countS[S[end]] >= 0:
                    count -= 1
                while count == 0:
                    match = 1
                    while start <= end:
                        if S[start] in countT:
                            countS[S[start]] += 1
                            if countS[S[start]] > 0:
                                break
                        start += 1
                    tmp = end-start+1
                    if tmp < minlength:
                        minstart, minlength = start, tmp
                    start += 1
                    count += 1    
            end += 1
        return "" if match == 0 else S[minstart:(minstart+minlength)]
                
         


##### 判断是否cover T需要比较2个dictionary,可能比较费时, 参考count的用法
class Solution:
    def checkCover(self, dictS, dictT):
        for ele in dictT.keys():
            if ele not in dictS or dictS[ele] < dictT[ele]:
                return False
        return True

    # @return a string
    def minWindow(self, S, T):
        countT={}; countS={}
        for char in T:
            if char not in countT: countT[char]=1
            else: countT[char]+=1
            
        start, end = 0, 0
        minstart, minend, minlength = 0, len(S)-1, len(S)
        match = 0
        while end < len(S) and start <= end:
            if S[end] not in countT.keys():
                end += 1
                continue
            elif S[end] in countT.keys() and S[end] not in countS:
                countS[S[end]] = 1
            else:
                countS[S[end]] += 1
            while self.checkCover(countS, countT):
                match = 1
                while S[start] not in countT.keys():
                    start += 1
                tmp = end-start+1
                if tmp < minlength:
                    minlength = tmp
                    minstart, minend = start, end
                    print minstart, minend
                countS[S[start]] -= 1
                start += 1
            end += 1
        return "" if match == 0 else S[minstart:(minend+1)]
                
         

class Solution:
    # @return a string
    def minWindow(self, S, T):
        count1={}; count2={}
        for char in T:
            if char not in count1: count1[char]=1
            else: count1[char]+=1
        for char in T:
            if char not in count2: count2[char]=1
            else: count2[char]+=1
        count=len(T)
        start=0; minSize=len(S); minStart=0
        for end in range(len(S)):
            if S[end] in count2 and count2[S[end]]>0:
                count1[S[end]]-=1
                if count1[S[end]]>=0:  ### 说明match到了一个有效字符 (当count1[S[end]] < 0 说明已经match到了足够的S[end], 这个不应该算)
                    count-=1
            if count==0: ### 完全match了 T
                while True:
                    if S[start] in count2 and count2[S[start]]>0:
                        if count1[S[start]]<0:
                            count1[S[start]]+=1
                        else: ### 若刚好 count1[S[start]] == 0: 则为了保持仍然cover T, 不移动start 
                        ### 通过 继续移动end, 来include T中的元素, 等到有足够多时才移动start, 因此不需要修改count的值. 同时最后也可以根据count==0 来判断是否S中存在一个substring完全cover T
                            break
                    start += 1
                if minSize>end-start+1:
                    minSize=end-start+1; minStart=start
        return "" if count != 0 else S[minStart:minStart+minSize]