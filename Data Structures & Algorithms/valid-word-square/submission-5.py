class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for n in range(len(words[i])):
                if n >= len(words) or i >= len(words[n]):
                    return False
                if words[i][n] != words[n][i]:
                    return False
        return True
