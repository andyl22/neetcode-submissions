class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        l = len(word1)
        r = len(word2)

        for i in range(min(l, r)):
            merged.extend([word1[i], word2[i]])

        return "".join(merged) + word1[i+1:] + word2[i+1:]