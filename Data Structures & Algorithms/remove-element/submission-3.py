class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if not nums:
            return 0

        count = 0

        for i in range(len(nums)):
            if nums[i] != val:
                count += 1
                continue 
        
            j = i + 1
            while j < len(nums) and nums[j] == val:
                j += 1
            
            if j < len(nums):
                nums[i], nums[j] = nums[j], nums[i]
                count += 1
            else:
                return count
        return count
                