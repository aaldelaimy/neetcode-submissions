class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for x in range(len(nums)):
            mult = 1
            for y in range(len(nums)):
                if y != x:
                    mult = (mult * nums[y])
            output.append(mult)
        return output