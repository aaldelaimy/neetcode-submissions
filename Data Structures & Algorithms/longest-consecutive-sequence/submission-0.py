class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            long = 0
            if (n - 1) not in numSet:
                while (n + long) in numSet:
                    long += 1
                longest = max(longest, long)
        return longest