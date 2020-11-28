class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        to100 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()

        def toWords(n):
            n = int(n)
            if n == 0:
                return 'Zero'
            if n < 20:
                return to19[n - 1:n]
            if n < 100:
                return [to100[n // 10 - 2]] + toWords(n % 10)
            if n < 1000:
                return [to19[n // 100 - 1]] + ["Hundred"] + toWords(n % 100)
            for i, p in enumerate(("Thousand", "Million", "Billion"), 1):
                    if n < 1000 ** (i + 1):
                        return toWords(n // 1000 ** i) + [p] + toWords(n % 1000 ** i)

        return 'Zero' if num == 0 else ' '.join(toWords(num))

if __name__ == '__main__':
    f = Solution()
    print(f.numberToWords(1317))