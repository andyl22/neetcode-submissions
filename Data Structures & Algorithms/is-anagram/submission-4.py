from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use Counter to count occurrences of characters in both strings
        return Counter(s) == Counter(t)