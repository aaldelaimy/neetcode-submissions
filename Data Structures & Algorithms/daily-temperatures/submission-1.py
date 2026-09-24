class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i, n in enumerate(temperatures):

            if stack:
                while stack and n > stack[-1][1]:
                    prevI, prevN = stack.pop()

                    res[prevI] = i - prevI
            
            stack.append((i, n))
        
        return res

