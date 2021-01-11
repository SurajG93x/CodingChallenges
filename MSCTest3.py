class Solution:
    def test(self, strin):
        ops = strin.split(" ")
        stack = []

        for op in ops:
            if op.isdigit():
                stack.append(int(op))
            elif op == "DUP":
                if not stack:
                    return -1
                stack.append(stack[-1])
            else:
                if len(stack) < 2:
                    return -1

                n1 = stack.pop()
                n2 = stack.pop()
                if op == "+":
                    num = n1+n2
                    if num > (2**31-1):
                        return -1
                    else:
                        stack.append(num)
                elif op == "-":
                    num = n1 - n2
                    if num < 0:
                        return -1
                    else:
                        stack.append(num)


        if not stack:
            return -1
        else:
            return stack.pop()


if __name__ == '__main__':
    f = Solution()
    print(f.test('3 DUP 5 - DUP'))