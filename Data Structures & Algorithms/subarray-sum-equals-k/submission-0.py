class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}

        count = 0
        t = 0
        for i in range(len(nums)):
            t += nums[i]

            remainder = t - k
            if remainder in prefix:
                count += prefix[remainder]
            prefix[t] = prefix.get(t, 0)+1
        return count