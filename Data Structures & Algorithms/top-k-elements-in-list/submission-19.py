class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []

        for num, freq in counts.items():
            heapq.heappush(res, (freq, num))
            if len(res) > k:
                heapq.heappop(res)
        
        return [v[1] for v in res]
