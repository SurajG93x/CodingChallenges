class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        tobedeleted = set()
        returnstr = []

        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            if c == ")":
                if not stack:
                    tobedeleted.add(i)
                else:
                    stack.pop()
        tobedeleted.union(set(stack))

        for i,c in enumerate(s):
            if i not in tobedeleted:
                returnstr.append(c)

        return "".join(returnstr)


if __name__ == '__main__':
    f = Solution()
    print(f.minRemoveToMakeValid("lee(t(c)o)de)"))