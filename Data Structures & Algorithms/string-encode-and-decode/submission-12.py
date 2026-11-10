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
            words.append(s[j+1:j+length+1])
            l = j+length+1
        return words
