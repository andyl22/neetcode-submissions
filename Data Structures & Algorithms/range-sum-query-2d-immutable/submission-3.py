class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]

        # 0, 0, 0
        # 0, 1, 2
        # 0, 3, 4

        # 0, 0, 0
        # 0, 1, 3
        # 0, 4, 10
        for r in range(len(matrix)):
            total = 0
            for c in range(len(matrix[r])):
                self.sums[r+1][c+1] = matrix[r][c] + self.sums[r+1][c] + self.sums[r][c+1] - self.sums[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2+1][col2+1] - self.sums[row1][col2+1] - self.sums[row2+1][col1] + self.sums[row1][col1] 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)