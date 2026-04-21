class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # a, b
        # c, d

        # a, a+b
        # a+c, (a+b) + (a+c) - a

        # 0 , 0, 0
        # 0 , a, a + b
        # 0, a + c , (a+b) + (a+c) - a
        R, C = len(matrix), len(matrix[0])

        self.sums = [[0] * (C + 1) for _ in range(R + 1)]

        for r in range(R):
            for c in range(C):
                self.sums[r+1][c+1] = (matrix[r][c] 
                + self.sums[r][c+1] 
                + self.sums[r+1][c] 
                - self.sums[r][c])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2+1][col2+1] - self.sums[row1][col2+1] - self.sums[row2+1][col1] + self.sums[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)