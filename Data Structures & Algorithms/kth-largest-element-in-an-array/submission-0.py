class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        pos = len(nums) - k

        for i in range(len(nums) - 1, -1, -1):
            if i == pos:
                return nums[i]