class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1,r+1]
            if s < target:
                l += 1
                while numbers[l-1] == numbers[l]:
                    l += 1
            else:
                r -= 1
                while numbers[r+1] == numbers[r]:
                    r-=1