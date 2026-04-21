class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)

        newWord = ""
        for i in range(min(n, m)):
            newWord += word1[i] + word2[i]
            
        return newWord + word1[i+1:] + word2[i+1:]