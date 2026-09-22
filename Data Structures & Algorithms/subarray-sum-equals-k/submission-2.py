class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        rSum = 0
        count = 0

        for i,v in enumerate(nums):
            rSum += v

            remainder = rSum - k
            if remainder in prefix:
                count += prefix[remainder]
            prefix[rSum] = prefix.get(rSum, 0) + 1
        return count