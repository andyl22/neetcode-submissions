class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        m = 0

        for n in nums:
            counter[n] += 1
            if counter[n] > counter[m]:
                m = n
        
        return m