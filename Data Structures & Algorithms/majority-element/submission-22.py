class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        best = [0, 0]

        for n in nums:
            if best[0] != n:
                best[1] -= 1
                if best[1] <= 0:
                    best = [n, 1]
            else:
                best[1] += 1

        
        return best[0]