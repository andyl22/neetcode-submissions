class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)
        for s in strs:
            counts = [0 for _ in range(26)]
        
            for c in s:
                counts[ord(c) - ord('a')] += 1
            buckets[str(counts)].append(s)
        
        return [v for v in buckets.values()]