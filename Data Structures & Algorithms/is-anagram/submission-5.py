class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Use two dictionaries to store character counts
        s_counts = {}
        t_counts = {}

        # 2. Count frequencies in the first string (s)
        for char in s:
            s_counts[char] = s_counts.get(char, 0) + 1
        
        # 3. Count frequencies in the second string (t)
        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1
        
        # 4. Final Comparison
        # Check if the two frequency maps (dictionaries) are identical
        return s_counts == t_counts
