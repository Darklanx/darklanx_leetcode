class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_to = [0 for i in range(len(cost) + 1)]
        for i in range(2, len(cost_to)):
            cost_to[i] = min(cost_to[i-1] + cost[i-1], cost_to[i-2] + cost[i-2])
        return cost_to[-1]