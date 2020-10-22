'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        op = 0
        sign = 1
        stack = []

        for i in s:
            if i.isdigit():
                op = op*10 + int(i)
            elif i == "+":
                res += sign*op
                sign = 1
                op = 0
            elif i == '-':
                res += sign*op
                sign = -1
                op =0
            elif i == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif i == ")":
                res += sign * op
                res *= stack.pop()
                res += stack.pop()
                op = 0

        return res + sign * op

if __name__ == '__main__':
    f = Solution()
    print(f.calculate("(1+(4+5+2)-3)+(6+8)"))