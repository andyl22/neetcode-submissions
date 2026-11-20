class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        freqMap = defaultdict(int)
        freq = 0
        best = 0

        while j < len(s):
            freqMap[s[j]] += 1
            freq = max(freq, freqMap[s[j]])
            if j - i + 1 - freq > k:
                freqMap[s[i]] -= 1
                i += 1
            best = j - i + 1
            j += 1
        return best
        