class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        hashmap = defaultdict(int)
        res = 0

        for r in range(len(s)):
            hashmap[s[r]] += 1

            subs = ((r - l) + 1) - (max(hashmap.values()))

            if subs <= k:
                res = max(res, (r - l) + 1)
            else:
                while subs > k:
                    hashmap[s[l]] -= 1
                    l += 1
                    subs = ((r - l) + 1) - (max(hashmap.values()))
        
        return res
