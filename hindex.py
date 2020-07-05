class Solution:
    def hIndex(self, citations):
        # total = len(citations)
        # min = 0
        #
        # for i in range(0, total):
        #     if citations[i] >= total - i:
        #         min = total - i
        # return min
        n = len(citations)
        for idx, c in enumerate(citations):
            if c >= n - idx:
                return n - idx
        return 0

if __name__ == '__main__':
    f = Solution()
    b = [0,1,3,5,6]
    print(f.hIndex(b))