class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []

        digitmap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        cur = []

        def backtrack(i):

            if len(cur) == len(digits):
                res.append(''.join(cur))
                return

            for c in digitmap[digits[i]]:
                cur.append(c)
                backtrack(i + 1)
                cur.pop()
        
        if digits:
            backtrack(0)
        
        return res
