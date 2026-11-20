class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = defaultdict(int)
        prefixMap[0] = 1

        rollingSum = 0
        count = 0
        for n in nums:
            rollingSum += n
            remainder = rollingSum - k
            if prefixMap[remainder]:
                count += prefixMap[remainder]
            
            prefixMap[rollingSum] += 1
        
        return count