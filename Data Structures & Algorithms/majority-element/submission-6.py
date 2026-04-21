class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = defaultdict(int)
        most = 0

        for n in nums:
            c[n] += 1
            if c[n] > c[most]:
                most = n
        
        return most