class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        for word in strs:

            key = [0] * 26

            for c in word:
                k = ord('z') - ord(c)
                key[k] += 1
            
            hashmap[tuple(key)].append(word)
        
        return list(hashmap.values())
