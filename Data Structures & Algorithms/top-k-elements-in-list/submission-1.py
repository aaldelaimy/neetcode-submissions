class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for x in nums:
            count[x] = 1 + count.get(x, 0)
        
        for x, cnt in count.items():
            freq[cnt].append(x)

        result = []

        for i in range (len(freq) - 1, 0, -1):
            for x in freq[i]:
                result.append(x)
            if len(result) == k:
                return result