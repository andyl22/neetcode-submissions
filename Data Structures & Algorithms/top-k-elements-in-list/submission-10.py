class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = [[] for _ in range(len(nums)+1)]
        freqMap = defaultdict(int)

        for n in nums:
            freqMap[n] += 1

        for key, value in freqMap.items():
            topK[value].append(key)
        
        res = []
        for l in range(len(topK)-1, -1, -1):
            for v in topK[l]:
                res.append(v)
                if(len(res)) == k:
                    return res