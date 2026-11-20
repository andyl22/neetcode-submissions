class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        res = []
        for i,v in counts.items():
            if v > float(len(nums)/3):
                res.append(i)
        return res