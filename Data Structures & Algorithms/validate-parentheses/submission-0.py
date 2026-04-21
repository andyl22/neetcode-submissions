class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        partner = {"(": ")", "{": "}", "[": "]"}

        for c in s:
            if c in partner: # If it's an opening bracket
                stack.append(c)
            else:
                # 1. Check if stack is empty before popping
                if not stack:
                    return False
                
                # 2. Pop and compare
                left_bracket = stack.pop()
                if partner[left_bracket] != c:
                    return False
        
        # 3. Ensure no unmatched opening brackets are left
        return len(stack) == 0