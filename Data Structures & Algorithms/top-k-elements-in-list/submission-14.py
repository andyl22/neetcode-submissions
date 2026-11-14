class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []
        buckets = [[] for _ in range(len(nums)+1)]
        for n, freq in counts.items():
            buckets[freq].append(n)
        
        for i in range(len(buckets)-1,-1, -1):
            for j in range(len(buckets[i])-1,-1,-1):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res
