class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {} 
        
        for i, x in enumerate(nums):
            diff = target - x

            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[x] = i