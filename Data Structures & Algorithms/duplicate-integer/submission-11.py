class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        visit = set()

        for x in nums:
            if x in visit:
                return True
            visit.add(x)
        return False