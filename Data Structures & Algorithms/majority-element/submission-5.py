class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = defaultdict(int)
        most = None

        for n in nums:
            c[n] += 1
            if most == None or c[n] > c[most]:
                most = n
        
        return most