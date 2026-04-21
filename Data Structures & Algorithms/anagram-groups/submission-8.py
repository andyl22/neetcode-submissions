class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)

        for s in strs:
            k = [0 for _ in range(26)]
            for c in s:
                k[ord(c) - ord('a')] += 1
            a[str(k)].append(s)
        
        return [v for v in a.values()]