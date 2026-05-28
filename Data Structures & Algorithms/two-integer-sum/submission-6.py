class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = {}

        for i, x in enumerate(nums):
            diff = target - x

            if diff in res:
                return [res[diff], i]
            
            res[x] = i