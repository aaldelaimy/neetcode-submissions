class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                
                if grid[r][c] == 1:
                    fresh += 1
        
        minutes = 0
        while q and fresh > 0:

            for _ in range(len(q)):
                r, c = q.popleft()
                

                if r + 1 < ROWS and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    q.append((r + 1, c))
                    fresh -= 1
                if r - 1 >= 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    q.append((r - 1, c))
                    fresh -=1
                if c + 1 < COLS and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    q.append((r, c + 1))
                    fresh -= 1
                if c - 1 >=0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    q.append((r, c - 1))
                    fresh -= 1
            
            minutes += 1
        
        if fresh == 0:
            return minutes
        else:
            return -1


