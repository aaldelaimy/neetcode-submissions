class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        minutes = 0
        while q and fresh > 0:

            for i in range(len(q)):

                r, c = q.popleft()

                if r + 1 < ROWS and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    fresh -= 1
                    q.append((r + 1, c))
                
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    fresh -= 1
                    q.append((r - 1, c))
                
                if c + 1 < COLS and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    fresh -= 1
                    q.append((r, c + 1))
                
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    fresh -= 1
                    q.append((r, c - 1))
            
            minutes += 1
        
        if fresh != 0:
            return -1
        
        return minutes

            

            