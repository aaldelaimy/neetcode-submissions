class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        emptySet = set()
        
        for num in nums:
            if num in emptySet:
                return True
            emptySet.add(num)
        return False