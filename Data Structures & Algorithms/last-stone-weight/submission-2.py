class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, v in enumerate(stones):
            stones[i] = -v
        heapq.heapify(stones)
        while len(stones) > 1:
            heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))
        
        return abs(heapq.heappop(stones))
        