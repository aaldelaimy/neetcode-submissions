class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s) != len(t):
            return False
        

        hashmapS = defaultdict(int)
        hashmapT = defaultdict(int)

        for i in range(len(s)):
            hashmapS[s[i]] += 1
            hashmapT[t[i]] += 1
        
        return hashmapS == hashmapT