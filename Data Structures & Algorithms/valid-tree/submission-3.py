class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        hashmap = defaultdict(list)

        for curr, nxt in edges:
            hashmap[curr].append(nxt)
            hashmap[nxt].append(curr)
        
        visit = set()
        
        def dfs(curr, prev):

            if curr in visit:
                return False
            
            visit.add(curr)
            
            for neighbor in hashmap[curr]:
                if neighbor == prev:
                    continue
                
                if not dfs(neighbor, curr):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visit)
