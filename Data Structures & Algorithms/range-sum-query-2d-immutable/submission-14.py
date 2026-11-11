class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        sums = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        for r in range(rows):
            for c in range(cols):
                sums[r+1][c+1] = matrix[r][c] + sums[r][c+1] + sums[r+1][c] - sums[r][c]
        self.sums = sums

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2+1][col2+1] - self.sums[row1][col2+1] - self.sums[row2+1][col1] + self.sums[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)