class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = max(len(num1), len(num2))
        num1 = num1.zfill(n)
        num2 = num2.zfill(n)
        nums = {}
        for i in range(0, 10):
            nums[str(i)] = i

        intN1 = 0
        intN2 = 0

        pl = 1
        for i in range(n - 1, -1, -1):
            intN1 += pl * nums[num1[i]]
            intN2 += pl * nums[num2[i]]
            pl *= 10

        return intN1 + intN2


if __name__ == '__main__':
    f = Solution()
    print(f.addStrings("0", "0"))