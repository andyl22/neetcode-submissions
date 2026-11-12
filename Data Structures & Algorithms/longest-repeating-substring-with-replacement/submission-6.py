class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, freq, freqMap = 0, 0, 0, defaultdict(int)
        best = 0

        while r < len(s):
            freqMap[s[r]] += 1
            freq = max(freq, freqMap[s[r]])
            while r - l - freq + 1 > k:
                freqMap[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
            r += 1
        return best

