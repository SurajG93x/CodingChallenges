class Solution:
    def maxProfit(self, k: int, prices) -> int:
        bp = sorted(prices)
        sp = sorted(prices, reverse=True)

        i = 0
        res = 0
        while i <= k:
            res += sp[i] - bp[i]
            i += 2

        return res


if __name__ == '__main__':
    f = Solution()
    k = 2
    prices = [2, 4, 1]
    print(f.maxProfit(k, prices))