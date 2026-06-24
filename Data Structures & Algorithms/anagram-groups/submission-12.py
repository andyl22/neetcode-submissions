class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)

        for s in strs:
            key = [0 for _ in range(26)]
            for c in s:
                key[ord(c)-ord('a')] += 1
            buckets[str(key)].append(s)
        
        return [v for v in buckets.values()]