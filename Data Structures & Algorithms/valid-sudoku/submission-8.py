class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # board should be a set of arrays that can be found with r // 3, c // 3
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        boards = [[[] for _ in range(3)] for _ in range(3)]

        for r in range(len(board)):
            for c in range(len(board[r])):
                cell = board[r][c]
                if cell == ".":
                    continue
                if (cell in rows[r]) or (cell in cols[c]) or (cell in boards[r//3][c//3]):
                    return False

                rows[r].append(cell)
                cols[c].append(cell)
                boards[r//3][c//3].append(cell)
        
        return True
                
