'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
'''

class Solution:
    def __init__(self):
        self.valid = None
        self.minRemoved = None

    def reset(self):
        self.valid = set()
        self.minRemoved = float('inf')

    def rem(self, string, idx, leftcount, rightcount, curr, removed):
        if idx == len(string):
            if leftcount == rightcount:
                if removed <= self.minRemoved:
                    ans = " ".join(curr)

                    if removed < self.minRemoved:
                        self.valid = set()
                        self.minRemoved = removed
                    self.valid.add(ans)

        else:
            currentChar = string[idx]

            if currentChar not in "()":
                curr.append(currentChar)
                self.rem(string, idx+1, leftcount, rightcount, curr, removed)
                curr.pop()

            else:
                self.rem(string, idx+1, leftcount, rightcount, curr, removed+1)
                curr.append(currentChar)

                if currentChar == "(":
                    self.rem(string, idx+1, leftcount+1, rightcount, curr, removed)
                elif rightcount < leftcount:
                    self.rem(string, idx+1, leftcount, rightcount+1, curr, removed)

                curr.pop()

    def removeInvalidParentheses(self, s):
        self.reset()

        self.rem(s, 0, 0, 0, [], 0)
        return list(self.valid)


if __name__ == '__main__':
    f = Solution()
    print(f.removeInvalidParentheses("()())()"))