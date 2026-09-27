class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        l, r = 1, max(piles)

        res = float('inf')

        while l <= r:

            m = (r + l) // 2

            total = 0
            for n in piles:
                total += math.ceil(n / m)
            
            if total <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res