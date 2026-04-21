class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # If s is empty, it's always a subsequence
        if not s:
            return True
            
        i = 0  # Pointer for s
        for char in t:
            # If characters match, move the s pointer
            if i < len(s) and s[i] == char:
                i += 1
        
        # If we reached the end of s, it's a subsequence
        return i == len(s)