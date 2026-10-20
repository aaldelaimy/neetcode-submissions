class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if not nums:
            return 0

        count = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1

        return count
                