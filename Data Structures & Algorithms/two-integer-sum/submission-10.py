class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = defaultdict(int)

        for i,n in enumerate(nums):
            r = target - n
            if r in remainder:
                return [remainder[r], i]
            remainder[n] = i
        