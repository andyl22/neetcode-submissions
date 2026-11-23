class Solution {
    public int lengthOfLongestSubstring(String s) {
        int slow = 0;
        int best = 0;
        Map<Character, Integer> jumpMap = new HashMap<>();

        for(int fast = 0; fast <s.length(); fast ++) {
            char fastChar = s.charAt(fast);
            if(jumpMap.containsKey(fastChar) && slow <= jumpMap.get(fastChar)) {
                slow = jumpMap.get(fastChar)+1;
            }
            best = Math.max(fast - slow + 1, best);
            jumpMap.put(fastChar, fast);
        }

        return best;
    }
}
