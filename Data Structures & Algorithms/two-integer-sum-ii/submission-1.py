class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while True:
            t = numbers[left] + numbers[right]
            if target == t:
                return [left+1, right+1]
            elif t > target:
                right -= 1
            else:
                left += 1