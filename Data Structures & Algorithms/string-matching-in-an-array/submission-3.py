class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if words[i] in words[j]:
                        if words[i] not in substrings:
                            substrings.append(words[i])
        return substrings