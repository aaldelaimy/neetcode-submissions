class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)
        bucket = [[] for _ in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] += 1
        
        for n, c in count.items():
            bucket[c].append(n)
        
        for i in range(len(bucket) -1, -1 ,-1):
            for n in bucket[i]:
                    res.append(n)
                    if len(res) == k:
                        return res