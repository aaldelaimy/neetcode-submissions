class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
    
        while q:
            
            for _ in range(len(q)):
                r, c, distance = q.popleft()

                
                if r + 1 < ROWS and grid[r + 1][c] == INF:
                    q.append((r + 1, c, distance + 1))
                    grid[r + 1][c] = distance + 1
                if r - 1 >= 0 and grid[r - 1][c] == INF:
                    q.append((r - 1, c, distance + 1))
                    grid[r - 1][c] = distance + 1
                if c + 1 < COLS and grid[r][c + 1] == INF:
                    q.append((r, c + 1, distance + 1))
                    grid[r][c + 1] = distance + 1
                if c - 1 >= 0 and grid[r][c - 1] == INF:
                    q.append((r, c - 1, distance + 1))
                    grid[r][c - 1] = distance + 1
            
        
