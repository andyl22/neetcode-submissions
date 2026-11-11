class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = []
        l = 0
        while l < len(word1) and l < len(word2):
            final.append(word1[l])
            final.append(word2[l])
            l += 1
        
        final.extend(word1[l:])
        final.extend(word2[l:])

        return "".join(final)