class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we need to find the window of fast - (slow+1) - freq > k
        # then we move slow up to reduce the character count 
        # until we find a window where subtracting by freq results in < k again

        slow = 0
        fast = 0
        freq = 0
        freqMap = defaultdict(int)
        best = 0

        while fast < len(s):
            freqMap[s[fast]] += 1
            freq = max(freqMap[s[fast]], freq)
            while fast - slow - freq + 1 > k:
                freqMap[s[slow]] -= 1 
                slow += 1
            best = max(best,fast-slow+1)
            fast += 1
        
        return best