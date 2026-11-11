class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rMap = defaultdict(int)
        rMap[0] = 1
        counter = 0
        rollingSum = 0

        for i in range(len(nums)):
            rollingSum += nums[i]
            remainder = rollingSum - k
            if rMap[remainder]:
                counter += rMap[remainder]
            
            rMap[rollingSum] += 1
        
        return counter