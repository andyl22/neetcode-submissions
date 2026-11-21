class Solution {
    public int lengthOfLongestSubstring(String s) {
        int slow = 0;
        Map<Character, Integer> seen = new HashMap<>();
        int best = 0;

        for(int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if (seen.containsKey(c) && slow < seen.get(c) + 1) {
                slow = seen.get(c) + 1;
            }
            seen.put(c, i);
            best = Math.max(best, i - slow + 1);
        }

        return best;
    }
}
