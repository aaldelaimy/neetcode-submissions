class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        countS1 = defaultdict(int)
        seen = defaultdict(int)
        
        for i in range(len(s1)):
            countS1[s1[i]] += 1
        
        l = 0

        for r in range(len(s2)):
            
            seen[s2[r]] += 1
            if (r - l + 1) == len(s1):
                if countS1 == seen:
                    return True
                else:
                    seen[s2[l]] -= 1

                    if seen[s2[l]] == 0:
                        del seen[s2[l]]

                    l += 1
            
        return False