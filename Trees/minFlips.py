class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        binA = "{0:b}".format(a)
        binB = "{0:b}".format(b)
        binC = "{0:b}".format(c)

        n = max(len(binA), len(binB), len(binC))
        binA = binA.zfill(n)
        binB = binB.zfill(n)
        binC = binC.zfill(n)

        countA = 0
        countB = 0

        for i in range(len(binC)):
            if binA[i] != binC[i]: countA += 1
            if binB[i] != binC[i]: countB += 1

        return min(countA, countB)

if __name__ == '__main__':
    f = Solution()
    print(f.minFlips(2, 6, 5))