class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        word = strs[0]

        res = ""
        for i, c in enumerate(word):

            for string in strs:

                if i >= len(string) or string[i] != c:
                    return res
                
            res += c
                
        
        return res
        
   

