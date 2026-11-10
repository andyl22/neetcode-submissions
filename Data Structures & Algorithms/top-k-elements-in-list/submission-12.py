class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]
        counts = Counter(nums)

        for key, value in counts.items():
            freq[value].append(key)
        
        res = []

        for i in range(len(freq)-1,-1,-1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res