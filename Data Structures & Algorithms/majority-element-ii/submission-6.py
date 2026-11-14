class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []
        for k,v in c.items():
            if float(v/len(nums)) >= .333333334:
                res.append(k)

        return res