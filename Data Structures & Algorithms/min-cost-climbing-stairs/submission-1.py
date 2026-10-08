class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        t1 = 0
        t2 = cost[n - 1]

        for i in range(n - 2, -1, -1):
            temp = min(cost[i] + t1, cost[i] + t2)
            t1= t2
            t2 = temp
        
        return min(t1, t2)