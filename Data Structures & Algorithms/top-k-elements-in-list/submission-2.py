class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countMap = {}
        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)
        
        heap = []
        for num in countMap.keys():
            heapq.heappush(heap, (countMap[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res