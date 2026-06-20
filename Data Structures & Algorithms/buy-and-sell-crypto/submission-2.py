class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        maxSum = 0

        for r in range(len(prices)):

            if prices[l] < prices[r]:
                maxSum = max(maxSum, prices[r] - prices[l])
            else:
                l = r
        
        return maxSum