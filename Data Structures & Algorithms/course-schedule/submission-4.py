class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visit = set()
        def dfs(i):

            if i in visit:
                return False
            

            visit.add(i)
            for pre in adj[i]:
                if not dfs(pre):
                    return False

            visit.remove(i)
            adj[i] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
