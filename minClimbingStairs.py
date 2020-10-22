class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost[0], cost[1])

        minCost = []
        minCost.append(cost[0])
        minCost.append(cost[1])

        for i in range(2, len(cost)):
            minCost.append(min(minCost[i - 1] + cost[i], minCost(i - 2) + cost[i]))

        return min(minCost[-1], minCost[-2])