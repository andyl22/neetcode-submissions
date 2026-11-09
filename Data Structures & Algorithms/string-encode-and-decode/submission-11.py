class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded 

    def decode(self, s: str) -> List[str]:
        l = 0
        words = []
        while l < len(s):
            j = l
            while s[j] != "#":
                j += 1
            
            length = int(s[l:j])
            
            j += 1
            words.append(s[j:j+length])
            l = j + length
        return words