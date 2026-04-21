class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. Guard Clause
        if not matrix or not matrix[0]:
            return False
            
        rows, cols = len(matrix), len(matrix[0])
        
        # 2. Find the potential row
        top, bot = 0, rows - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:    # Target is bigger than this row's max
                top = row + 1
            elif target < matrix[row][0]:   # Target is smaller than this row's min
                bot = row - 1
            else:                           # Target is within this row's range
                break
        else:
            return False # Target not in any row range

        # 3. Binary search within that specific row
        row = (top + bot) // 2
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False