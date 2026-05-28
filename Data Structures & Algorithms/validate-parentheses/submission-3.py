class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for ch in s:
            if ch not in hashMap:
                stack.append(ch)
            elif stack and hashMap[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        else:
            return False