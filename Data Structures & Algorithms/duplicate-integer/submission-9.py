class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        tempSet = set()

        for x in nums:
            if x in tempSet:
                return True
            tempSet.add(x)
        return False