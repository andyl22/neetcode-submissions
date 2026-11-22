class Solution {
    public int characterReplacement(String s, int k) {
        int slow = 0;
        int freq = 0;
        int best = 0;
        Map<Character, Integer> freqMap = new HashMap<>();

        for (int i = 0; i<s.length(); i++) {
            Character c = s.charAt(i);
            freqMap.put(c, freqMap.getOrDefault(c,0) +1);
            freq = Math.max(freq, freqMap.get(c));
            if(i - slow + 1 - freq > k) {
                Character decrementKey = s.charAt(slow);
                freqMap.put(decrementKey, freqMap.get(decrementKey)-1);
                slow++;
            }
            best = Math.max(best, i - slow + 1);
        }
        return best;
    }
}
