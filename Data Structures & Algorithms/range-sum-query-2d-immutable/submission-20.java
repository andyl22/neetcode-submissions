class NumMatrix {
    private int[][] sumMatrix;
    public NumMatrix(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        sumMatrix = new int[rows + 1][cols + 1];

        for (int r = 0; r<rows; r++) {
            for (int c = 0; c < cols; c++) {
                sumMatrix[r+1][c+1] = matrix[r][c] + sumMatrix[r][c+1] + sumMatrix[r+1][c] - sumMatrix[r][c];
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        return sumMatrix[row2+1][col2+1] - sumMatrix[row2+1][col1] - sumMatrix[row1][col2+1] + sumMatrix[row1][col1];
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */