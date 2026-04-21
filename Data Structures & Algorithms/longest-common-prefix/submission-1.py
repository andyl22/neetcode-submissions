class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        b_prefix = strs[0]

        for s in strs:
            while b_prefix not in s:
                b_prefix = b_prefix[:-1]
                #early exit
                if not b_prefix:
                    return b_prefix

        return b_prefix