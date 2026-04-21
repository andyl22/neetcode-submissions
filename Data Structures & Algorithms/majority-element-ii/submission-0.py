class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = defaultdict(int)

        for n in nums:
            c[n] += 1
        res = []
        for k,v in c.items():
            if float(v) > len(nums)/3:
                res.append(k)
        return res