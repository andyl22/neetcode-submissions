class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        topK = [[] for _ in range(len(nums)+1)]

        for key,value in freqMap.items():
            topK[value].append(key)
        
        ans = []

        for l in reversed(topK):
            for v in l:
                ans.append(v)
                if len(ans) == k:
                    return ans
