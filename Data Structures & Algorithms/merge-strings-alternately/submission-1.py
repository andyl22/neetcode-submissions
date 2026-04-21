class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        output = ""

        while i < len(word1) and j < len(word2):
            output += word1[i] + word2[j]
            i += 1
            j += 1
        
        output += word1[i:] + word2[j:]
        return output
            