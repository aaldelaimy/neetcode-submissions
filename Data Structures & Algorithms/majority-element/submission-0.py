class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1
        
        return max(hashmap, key=hashmap.get)