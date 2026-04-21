class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        best = 0
        freq = 0
        count = defaultdict(int)

        for j in range(len(s)):
            char = s[j]
            count[char] += 1
            freq = max(count[char], freq)

            while j - i + 1 - freq > k:
                count[s[i]] -= 1
                i += 1
            best = max(best, j-i+1)
        
        return best