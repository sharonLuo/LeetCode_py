"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


注意!!!
这道题是经典的逆波兰式求值。具体思路是：开辟一个空栈，遇到数字压栈，遇到运算符弹出栈中的两个数进行运算，
并将运算结果压栈，最后栈中只剩下一个数时，就是所求结果。
这里需要注意的一点是python中的'/'除法和c语言不太一样。
在python中，(-1)/2=-1，而在c语言中，(-1)/2=0。
也就是c语言中，除法是向零取整，即舍弃小数点后的数。
而在python中，是向下取整的。
而这道题的oj是默认的c语言中的语法，所以需要在遇到'/'的时候注意一下。  
""" 


#### iterative Time O(n), Space O(logn)
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for inx in range(len(tokens)):
            if tokens[inx] != "*" and tokens[inx] != "/" and tokens[inx] != "+" and tokens[inx]!="-":
                stack.append(int(tokens[inx]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if tokens[inx] == "+":
                    stack.append(num1+num2)
                elif tokens[inx] == "-":
                    stack.append(num1-num2)
                elif tokens[inx] == "*":
                    stack.append(num1*num2)
                elif tokens[inx] == "/":
                    if num1*num2 < 0:
                        stack.append(-((-num1)/num2))
                    else:
                        stack.append(num1/num2)
        return stack.pop()
        