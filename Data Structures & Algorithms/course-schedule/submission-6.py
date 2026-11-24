class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for crs, pre in prerequisites:
            adj[crs].append(pre)
        

        visit = set()
        done = set()
        def dfs(crs):
            if crs in visit:
                return False

            if crs in done:
                return True

            visit.add(crs)

            for pre in adj[crs]:
                if not dfs(pre):
                    return False

            visit.remove(crs)
            done.add(crs)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True