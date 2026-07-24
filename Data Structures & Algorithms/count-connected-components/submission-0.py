class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        hashmap = defaultdict(list)

        for curr, neighbor in edges:
            hashmap[curr].append(neighbor)
            hashmap[neighbor].append(curr)
        
        visit = set()

        def dfs(curr):
            nonlocal visit

            if curr in visit:
                return
            
            visit.add(curr)
            for neighbor in hashmap[curr]:
                dfs(neighbor)
        
        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        
        return res
            
