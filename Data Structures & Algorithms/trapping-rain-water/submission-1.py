class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1

        res = 0
        maxL = 0
        maxR = 0

        while l < r:
        
            maxL = max(height[l], maxL)
            maxR = max(height[r], maxR)

            if height[r] < height[l]:
                r -= 1
                if maxR > height[r]:
                    res += (maxR - height[r])
            else:
                l += 1
                if maxL > height[l]:
                    res += (maxL - height[l])
        
        return res
