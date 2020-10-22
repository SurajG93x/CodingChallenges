'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:
    def generateParenthesis(self, n):
        left,right = n,n
        res = []

        self.dfs(left,right,res,"")
        return res

    def dfs(self, left, right, res, curr):
        if right < left: return                         #because you can't add a ( if there no ) to pair it with before
        if not left and not right: res.append(curr)     #when left and right are empty, you have a valid string
        if left: self.dfs(left-1,right,res,curr+'(')    #as long as left isn't empty
        if right: self.dfs(left,right-1,res,curr+')')

if __name__ == '__main__':
    f = Solution()
    print(f.generateParenthesis(3))