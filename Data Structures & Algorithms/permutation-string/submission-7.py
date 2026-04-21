class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = defaultdict(int)

        i = 0
        matches = 0
        expected = len(c1)
        wSize = len(s1)

        for j in range(len(s2)):
            char = s2[j]
            c2[char] += 1
            
            if char in c1:
                if c2[char] == c1[char]:
                    matches += 1
                elif c2[char] == c1[char] + 1:  # count went above expected
                    matches -= 1

            if j - i + 1 > wSize:
                lChar = s2[i]
                if lChar in c1:
                    if c2[lChar] == c1[lChar]:
                        matches -= 1
                    elif c2[lChar] == c1[lChar] + 1:
                        matches += 1
                c2[lChar] -= 1
                i += 1
            
            if matches == expected:
                return True
        
        return False

