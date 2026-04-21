class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = defaultdict(int)
        most = None

        for n in nums:
            m[n] += 1
            if m[most] < m[n]:
                most = n
        
        return most