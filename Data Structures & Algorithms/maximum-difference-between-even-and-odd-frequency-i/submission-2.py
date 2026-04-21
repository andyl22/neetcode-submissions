class Solution:
    def maxDifference(self, s: str) -> int:
        counter = defaultdict(int)

        for c in s:
            counter[c] += 1
        
        bestOdd = 0
        bestEven = 10000
        for v in counter.values():
            if v%2:
                bestOdd = max(bestOdd, v)
            else:
                bestEven = min(bestEven, v)
        
        return bestOdd - bestEven