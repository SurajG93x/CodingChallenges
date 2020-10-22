class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        outStack = []
        stack = []
        delIdx = []
        res = ""

        for i in range(len(S)):
            if S[i] == "(":
                if not outStack:
                    outStack.append(i)
                else:
                    stack.append(i)
            elif S[i] == ")":
                if stack:
                    stack.pop()
                elif outStack:
                    delIdx.append(outStack.pop())
                    delIdx.append(i)

        for i in range(len(S)):
            if i not in delIdx:
                res += S[i]

        return res

if __name__ == '__main__':
    f = Solution()
    print(f.removeOuterParentheses("(()())(())"))