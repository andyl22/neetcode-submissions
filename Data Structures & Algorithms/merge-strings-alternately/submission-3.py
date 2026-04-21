class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        l = 0
        r = 0

        while l < len(word1) and r < len(word2):
            if l <= r:
                merged.append(word1[l])
                l += 1
            else:
                merged.append(word2[r])
                r += 1

        return "".join(merged) + word1[l:] + word2[r:]