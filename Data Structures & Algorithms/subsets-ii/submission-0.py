class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        nums.sort()
        seen = set()

        def dfs(i):

            if i >= len(nums):
                if tuple(subset.copy()) not in seen:
                    res.append(subset.copy())
                    seen.add(tuple(subset.copy()))
                    return
                else:
                    return
            
            
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res