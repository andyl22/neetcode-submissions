class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        l = 0
        r = len(matrix) - 1

        # Step 1: Find the candidate row using the first element of each row
        while l <= r:
            mid = (r + l) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        # i is the row we want to search
        i = l - 1
        
        # SAFETY CHECK: If i < 0, target is smaller than the smallest element in the matrix
        if i < 0:
            return False

        # Step 2: Binary search inside that specific row
        l = 0 
        r = len(matrix[i]) - 1

        while l <= r:
            mid = (r + l) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False