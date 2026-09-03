class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1] 
            elif s > target:
                r -= 1
                while l < r and numbers[r + 1] == numbers[r]:
                    r -= 1
            else:
                l += 1
                while l < r and numbers[l - 1] == numbers[l]:
                    l += 1