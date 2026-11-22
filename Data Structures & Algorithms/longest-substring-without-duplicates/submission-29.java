class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> jumpMap = new HashMap<>();
        int slow = 0;
        int best = 0;

        for(int i =0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if(jumpMap.containsKey(c) && slow <= jumpMap.get(c)) {
                slow = jumpMap.get(c) + 1;
            }
            best = Math.max(i - slow + 1, best);
            jumpMap.put(c,i);
        }
        return best;
    }
}
