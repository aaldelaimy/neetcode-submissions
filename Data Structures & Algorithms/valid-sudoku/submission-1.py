class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ROWS, COLS = len(board), len(board[0])

        seenRow = defaultdict(set)
        seenCol = defaultdict(set)
        seenSquare = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                
                if board[r][c] == ".":
                    continue
                
                square = (r // 3, c // 3)
                if (
                    board[r][c] in seenRow[r] or 
                    board[r][c] in seenCol[c] or 
                    board[r][c] in seenSquare[square]):
                    return False
                
                seenRow[r].add(board[r][c])
                seenCol[c].add(board[r][c])
                seenSquare[square].add(board[r][c])
                
        return True