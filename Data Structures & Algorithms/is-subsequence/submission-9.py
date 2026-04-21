import bisect

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        self.char_map = defaultdict(list)
        for index, char in enumerate(t):
            self.char_map[char].append(index)
        
        current_position = -1
        
        for char in s:
            if char not in self.char_map:
                return False  # Char doesn't exist in t at all
            
            # Find the first index in t that is > current_position
            indices = self.char_map[char]
            idx_in_list = bisect.bisect_right(indices, current_position)
            
            # If no such index exists, s is not a subsequence
            if idx_in_list == len(indices):
                return False
            
            # Move our marker to the index we just found
            current_position = indices[idx_in_list]
            
        return True

        ## If s is empty, it's always a subsequence
        # if not s:
        #     return True
        # i=0
        # for c in t:
        #     if c == s[i]:
        #         i += 1
        #         if i == len(s):
        #             return True

        # return i == len(s)
