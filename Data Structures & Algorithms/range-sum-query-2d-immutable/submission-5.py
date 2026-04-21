class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        #PATTERN: The Ruler (Padding)
        # We create an (R+1)x(C+1) 'frame' of zeros.
        # This 'Line 0' handles out-of-bounds cases automatically.
        R, C = len(matrix), len(matrix[0])

        self.sums = [[0] * (C + 1) for _ in range(R + 1)]

        for r in range(R):
            for c in range(C):
                self.sums[r+1][c+1] = (matrix[r][c] 
                + self.sums[r][c+1] 
                + self.sums[r+1][c] 
                - self.sums[r][c])
        
    # PATTERN: Inclusion-Exclusion (The "Dough Carving" Method)
    # To get the sum of a box, take the 'Big Rectangle' and subtract 
    # the 'Shadows' (slabs) above and to the left of it.

    # Coordinates:
    # (r2+1, c2+1) is the Bottom-Right "End Line"
    # (r1, c2+1)   is the Top "Cut Line" (Subtract everything above r1)
    # (r2+1, c1)   is the Left "Cut Line" (Subtract everything left of c1)
    # (r1, c1)      is the "Safety Corner" (Add back because it was cut twice)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2+1][col2+1] - self.sums[row1][col2+1] - self.sums[row2+1][col1] + self.sums[row1][col1]

    # 0 , 0, 0
    # 0 , a, a + b
    # 0, a + c , (a+b) + (a+c) - a

    # when we need subregion, reverse the above formula
    # cur - (a+b) - (a+c) + a
    # if we pass (1,1) since we are 0 padded, we really need (2,1 -- a + c) and (1, 2 -- a + b)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)