class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        adj = defaultdict(list)

        for curr, nxt in edges:
            adj[curr].append(nxt)
            adj[nxt].append(curr)
        
        visit = set()

        def dfs(curr):

            if curr in visit:
                return

            visit.add(curr)

            for neighbor in adj[curr]:

                if neighbor in visit:
                    continue
                
                dfs(neighbor)
        
        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        
        return res
                