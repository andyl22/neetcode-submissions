class Solution {
    public int lengthOfLongestSubstring(String s) {
        int slow = 0;
        Set<Character> seen = new HashSet<>();
        int best = 0;

        for(int i = 0; i < s.length(); i++) {
            while (seen.contains(s.charAt(i))) {
                seen.remove(s.charAt(slow));
                slow++;
            }
            seen.add(s.charAt(i));
            best = Math.max(best, i - slow + 1);
        }

        return best;
    }
}
