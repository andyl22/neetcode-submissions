class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we need a sliding window where we can have up to "k" characters or different values
        # when we detect a non acceptable amount of deviation, shrink the window until its valid
        # we need 2 pointers because we can't do a simple end of window - k
        # max (longest, j - i)

        left = 0
        freq = 0
        longest = 0
        count = defaultdict(int)

        for right in range(len(s)):
            char = s[right]
            count[char] += 1
            freq = max(count[char], freq)

            # [a,a,a,b,c,a], k =1
            # freq = a, right = 4, 4-0-3... 1 !> 1
            # freq = a, right = 5, 5-0-3... 2 > 1
            while (right - left + 1) - freq > k:
                count[s[left]] -= 1
                left += 1
            
            longest=max(longest,right-left+1)
        return longest