
class Solution:
    def MissingDigit(self,strParam):
        exp = list(strParam.split())

        op1 = exp[0]
        op2 = exp[2]
        operator = exp[1]
        ans = exp[-1]

        if 'x' in ans:
            x = ans
            op1 = int(op1)
            op2 = int(op2)

            if operator == '+':
                res = op1+op2
            elif operator == '-':
                res = op1-op2
            elif operator == '*':
                res = op1*op2
            elif operator == '/':
                res = op1//op2

        else:
            ans = int(ans)

            if 'x' in op1:
                x = op1
                op2 = int(op2)

                if operator == '+':
                    res = ans - op2
                elif operator == '-':
                    res = ans + op2
                elif operator == '*':
                    res = ans // op2
                elif operator == '/':
                    res = ans * op2

            else:
                x = op2
                op1 = int(op1)

                if operator == '+':
                    res = ans - op1
                elif operator == '-':
                    res = op1 - ans
                elif operator == '*':
                    res = ans // op1
                elif operator == '/':
                    res = op1 // ans

        res = str(res)
        k = 0
        for i in x:
            if i == 'x':
                result = res[k]
                break
            else:
                k = k+1

        return result


if __name__ == '__main__':
    f = Solution()
    print(f.MissingDigit('34 + x = 46'))