class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        j = len(numbers)-1

        while l < j:
            s = numbers[l] + numbers[j]
            if s == target:
                return [l+1,j+1]

            if s < target:
                l += 1
            else:
                j -= 1