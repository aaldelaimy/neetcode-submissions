class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        seen = set()
        cycle = set()
        output = []
        def dfs(crs):

            if crs in cycle:
                return False
            
            if crs in seen:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            output.append(crs)
            seen.add(crs)

            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        
        return output
            

