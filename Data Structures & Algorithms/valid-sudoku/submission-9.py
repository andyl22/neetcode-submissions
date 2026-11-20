class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boards = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                elif v in rows[r] or v in cols[c] or v in boards[r//3][c//3]:
                    return False
                rows[r].add(v)
                cols[c].add(v)
                boards[r//3][c//3].add(v)
        return True