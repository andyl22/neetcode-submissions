class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slow = 0
        longest = 0
        # most freq to track the dominant
        mostFreq = 0
        freq = defaultdict(int)

        for i in range(len(s)):
            char = s[i]
            freq[char] += 1
            mostFreq = max(mostFreq,freq[char])

            while i - slow + 1 - mostFreq > k:
                freq[s[slow]] -= 1
                slow += 1
            longest = max(longest, i - slow + 1)
        
        return longest