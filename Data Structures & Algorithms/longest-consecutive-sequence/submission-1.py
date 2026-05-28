class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0

        for n in nums:
            long = 0
            if (n - 1) not in hashSet:
                while (n + long) in hashSet:
                    long += 1
                longest = max(long, longest)
        return longest