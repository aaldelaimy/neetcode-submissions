class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:

            m = (top + bot) // 2

            if matrix[m][-1] < target:
                top = m + 1
            elif matrix[m][0] > target:
                bot = m - 1
            else:
                break
        
        row = m
        l, r = 0, COLS - 1

        while l <= r:

            m = (l + r) // 2

            if matrix[row][m] == target:
                return True

            if matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False

