class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = ""

        for word in strs:
            curr = str(len(word)) + "#" + word
            res += curr

        return res

    def decode(self, s: str) -> List[str]:
        
        # 5#Hello5#World

        res = []

        i = 0

        while i < len(s):
            j = i
            curr = ""
            while s[j] != "#":
                curr += s[j]
                j += 1

            length = int(curr)
            j += 1
            word = s[j:j + length]
            res.append(word)
            i = j + length
        
        return res

