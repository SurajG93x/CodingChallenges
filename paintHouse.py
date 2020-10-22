class Solution:
    def minCost(self, costs):
        self.memotable = {}

        def paint(n, color):
            if (n, color) in self.memotable:
                return self.memotable[(n, color)]
            cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0:
                cost += min(paint(n + 1, 1), paint(n + 1, 2))
            elif color == 1:
                cost += min(paint(n + 1, 0), paint(n + 1, 2))
            elif color == 2:
                cost += min(paint(n + 1, 1), paint(n + 1, 0))

            self.memotable[(n, color)] = cost
            return cost

        if costs == []: return 0

        return min(paint(0, 0), paint(0, 1), paint(0, 2))


if __name__ == '__main__':
    f = Solution()
    print(f.minCost([[17,2,17],[16,16,5],[14,3,19]]))