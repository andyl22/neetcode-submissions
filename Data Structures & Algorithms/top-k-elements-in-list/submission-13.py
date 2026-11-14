class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        my_heap = []
        for n, freq in counts.items():
            heapq.heappush(my_heap, (freq, n))
            if len(my_heap) > k:
                heapq.heappop(my_heap)

        return [v[1] for v in my_heap]