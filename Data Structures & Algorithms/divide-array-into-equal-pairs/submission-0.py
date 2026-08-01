class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1
        
        for count in hashmap.values():
            if count % 2 != 0:
                return False
            
        return True