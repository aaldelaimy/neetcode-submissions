class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        maxSum = 0

        for r in range(1, len(prices)):

            if prices[l] < prices[r]:
                maxSum = max(maxSum, prices[r] - prices[l])
            else:
                l = r
        
        return maxSum