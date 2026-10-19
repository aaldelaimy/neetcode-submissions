class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        word = strs[0]

        res = ""
        for i, c in enumerate(word):
            
            same = True

            for string in strs:

                if i >= len(string) or string[i] != c:
                    same = False
                    
            if same == True:
                res += c
            else:
                return res
        
        return res
        
   

