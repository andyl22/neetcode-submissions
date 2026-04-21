class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        res = []
        self.iterate(numRows, res)
        return res

    def iterate(self, n, res):
        # 1. Base Case: Return the first row to start the chain
        if n == 1:
            row = [1]
            res.append(row)
            return row

        # 2. Recursive Call: Get the row from the level below
        lastRow = self.iterate(n - 1, res)

        # 3. Build the new row using the 'sliding window' sum
        newRow = [1] # Every row starts with 1
        for i in range(len(lastRow) - 1):
            newRow.append(lastRow[i] + lastRow[i+1])
        newRow.append(1) # Every row ends with 1

        # 4. Add to result and return it to the call waiting above
        res.append(newRow)
        return newRow