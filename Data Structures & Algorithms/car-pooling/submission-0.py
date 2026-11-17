class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        hashmap = defaultdict(int)

        for n, start, end in trips:
            hashmap[start] += n
            hashmap[end] -= n

        count = 0
        for key in sorted(hashmap):
            count += hashmap[key]

            if count > capacity:
                return False
        
        return True