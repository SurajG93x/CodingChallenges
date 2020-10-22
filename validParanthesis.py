class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            elif (x == ')' or x == '}' or x == ']') and stack:
                y = stack.pop()
                if x == ')' and y == '(':
                    continue
                elif x == '}' and y == '{':
                    continue
                elif x == ']' and y == '[':
                    continue
                else:
                    return False
            else:
                return False

        return False if stack else True

if __name__ == '__main__':
    f = Solution()
    print(f.isValid("){"))