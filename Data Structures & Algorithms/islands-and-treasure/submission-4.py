class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        step = 0
        visit = set()

        while q:

            for _ in range(len(q)):
                r, c = q.popleft()

                if (
                    r < 0 or r >= ROWS or
                    c < 0 or c >= COLS or
                    grid[r][c] == -1 or 
                    (r, c) in visit
                ):
                    continue

                visit.add((r, c))

                if grid[r][c] == INF:
                    grid[r][c] = step
                
                q.append((r + 1, c))
                q.append((r - 1, c))
                q.append((r, c + 1))
                q.append((r, c - 1))
            
            step += 1
        
        
