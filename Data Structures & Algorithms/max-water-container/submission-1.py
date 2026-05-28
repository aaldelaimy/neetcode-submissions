class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maximum = float("-inf")
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[r], heights[l]) * (r - l)

            maximum = max(area, maximum)

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return maximum