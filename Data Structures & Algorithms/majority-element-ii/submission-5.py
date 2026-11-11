class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nCount = Counter(nums)
        res = []
        threshold = len(nums)/3
        for k,v in nCount.items():
            if float(v) > threshold:
                res.append(k)
        return res