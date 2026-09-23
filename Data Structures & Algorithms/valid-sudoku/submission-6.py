class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)

        for row in range(9):
            for col in range(9):
                cur = board[row][col]
                if cur == ".":
                    continue
                if cur in rows[row] or cur in cols[col] or cur in grids[row//3,col//3]:
                    return False
                rows[row].add(cur)
                cols[col].add(cur)
                grids[row//3,col//3].add(cur)
        
        return True