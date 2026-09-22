class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = [[] for _ in range(len(nums)+1)]
        nCounter = Counter(nums)

        for key,value in nCounter.items():
            topK[value].append(key)

        res = []

        for l in range(len(topK)-1, -1, -1):
            for v in topK[l]:
                res.append(v)
                if (len(res)) == k:
                    return res
