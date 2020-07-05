class Solution:
    def twoCitySchedCost(self, costs):
        a = sorted(costs, key=lambda x: x[0] - x[1])
        Sa = 0
        Sb = 0
        for i in range(len(a) // 2):
            Sa += a[i][0]

        for i in range(len(a) // 2, len(a)):
            Sb += a[i][1]
        return Sa + Sb

if __name__ == '__main__':
    f = Solution()
    print(f.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
