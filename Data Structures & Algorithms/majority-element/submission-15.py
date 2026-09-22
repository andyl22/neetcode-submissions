class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        m = defaultdict(int)

        for i,v in enumerate(nums):
            m[v] += 1
            majority = v if m[v] > m[majority] else majority
            
        return majority