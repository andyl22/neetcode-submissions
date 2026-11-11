class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rMap = {0: 1}
        count = 0
        rollingSum = 0

        for i,v in enumerate(nums):
            rollingSum += v

            remainder = rollingSum - k
            if remainder in rMap:
                count += rMap[remainder]
            rMap[rollingSum] = rMap.get(rollingSum, 0) + 1

        return count