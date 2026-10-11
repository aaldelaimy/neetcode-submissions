class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):

            if (
                r >= ROWS or r < 0 or
                c >= COLS or c < 0 or
                grid[r][c] == 0
            ):
                return 0

            grid[r][c] = 0
            up = dfs(r + 1, c)
            down = dfs(r - 1, c)
            right = dfs(r, c + 1)
            left = dfs(r, c - 1)

            return 1 + up + down + left + right

            
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(res, area)
        
        return res
                
