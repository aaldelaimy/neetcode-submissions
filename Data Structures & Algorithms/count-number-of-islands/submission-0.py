class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [[1,0], [-1, 0], [0, 1], [0,-1]]
        Rows, Cols = len(grid), len(grid[0])
        visit = set()
        islands = 0


        def bfs(start_r, start_c):
            q = deque()
            q.append((start_r, start_c))
            visit.add((start_r, start_c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    
                    if (0 <= nr and nr < Rows and
                        0 <= nc and nc < Cols and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visit
                    ):
                        q.append((nr, nc))
                        visit.add((nr,nc))

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands

        