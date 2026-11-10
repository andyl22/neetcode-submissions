class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded 

    def decode(self, s: str) -> List[str]:
        l = 0
        words = []
        while l < len(s)-1:
            j = l
            while s[j] != "#":
                j += 1
            
            length = int(s[l:j])
            j+=1
            end = j + length
            words.append(s[j:end])
            l = end
        return words
