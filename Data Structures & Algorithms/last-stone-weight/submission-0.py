class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap)>1:
            s1 = heapq.heappop(max_heap)
            s2 = heapq.heappop(max_heap)
            res = s1 - s2
            if res == 0:
                continue
            else:
             heapq.heappush(max_heap, res)
        
        return -max_heap[0] if len(max_heap) else 0
