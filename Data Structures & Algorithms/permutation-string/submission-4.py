class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = Counter(s1)
        freq2 = defaultdict(int)
        
        matches = 0
        perfectMatches = len(freq1)
        
        left = 0
        lenS1 = len(s1)
        for right in range(len(s2)):
            curChar = s2[right]
            freq2[curChar] += 1
            if freq2[curChar] == freq1[curChar]:
                matches += 1
            
            while right - left + 1 > lenS1:
                delChar = s2[left]
                if freq2[delChar] == freq1[delChar]:
                    matches -= 1
                freq2[delChar] -= 1
                left += 1
            
            if perfectMatches == matches:
                return True
        
        return False
                