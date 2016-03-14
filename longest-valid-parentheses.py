"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

"""



###### Solution 1
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        maxlen = 0
        stack = []
        last = -1
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)     # push the INDEX into the stack!!!!
            else:
                if stack == []:
                    last = i
                else:
                    stack.pop()
                    if stack == []:
                        maxlen = max(maxlen, i-last)
                    else:
                        maxlen = max(maxlen, i-stack[len(stack)-1])
        return maxlen

### solution 1.1
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        maxlen = 0
        stack = []
        last = -1
        for inx in range(len(s)):
            if s[inx] == "(":
                stack.append(inx)
            elif s[inx] == ")" and len(stack) == 0:
                last = inx
            else:
                stack.pop()
                if stack == []:
                    maxlen = max(maxlen, inx-last)
                else:
                    maxlen = max(maxlen, inx-stack[len(stack)-1])
        return maxlen
            
##### Solution 2 Dynamic Programming (很多边界问题要注意)
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if len(s) < 2:
            return 0
        dp = [0]*len(s)
        for inx in range(len(s)):
        	### 如果没有inx-1 >= 0, 则")("输出为2
            if s[inx] == ")" and inx-1 >=0 and s[inx-1] == "(":  
                dp[inx] = dp[inx-2]+2
            ### 同样这里需要保证 inx-dp[inx-1]-2 >= 0
            elif s[inx]==")" and s[inx-1] == ")" and (inx-dp[inx-1]-1 >= 0) and s[inx-dp[inx-1]-1]== "(":
                if inx - dp[inx-1] - 2 >=0 :
                    dp[inx] = dp[inx-1]+2+dp[inx-dp[inx-1]-2]
                else:
                    dp[inx] = dp[inx-1]+2
        return max(dp)    
            
                    
#### Solution 3: 两边扫描法
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        answer = 0
        depth = 0

        ### 完成对出现多余")"情况的查找
        start = -1
        for inx in range(len(s)):
            if s[inx] == "(":
                depth += 1
            else:
                depth -= 1
                if depth < 0:
                    start = inx
                    depth = 0
                elif depth == 0: ### 仅当depth == 0时才计算并更新max length
                    answer = max(answer, inx-start)
        
        ### 完成对出现多余"("情况的查找
        depth = 0
        start = len(s)
        for inx in range(len(s)-1, -1, -1):
            if s[inx] == ")":
                depth += 1
            else:
                depth -= 1
                if depth < 0:
                    start = inx
                    depth = 0
                elif depth == 0: ### 仅当depth == 0时才计算并更新max length
                    answer = max(answer, start-inx)
        
        return answer
                
        
        
                    
        
                

                
        