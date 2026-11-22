class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        int r = (rows * cols)-1;
        int l = 0;

        while (l<=r) {
            int mid = l + (r-l)/2;
            int[] cell = new int[2];
            cell[0] = mid/cols;
            cell[1] = mid%cols;
            int v=matrix[cell[0]][cell[1]];
            if(v==target) {
                return true;
            } else if(v<target) {
                l = mid+1;
            } else {
                r=mid-1;
            }
        }

        return false;
    }
}
