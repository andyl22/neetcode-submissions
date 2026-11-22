class Solution {
    public int characterReplacement(String s, int k) {
        int slow = 0;
        Map<Character, Integer> freqMap = new HashMap<>();
        int freq = 0;
        int best = 0;

        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
            freq = Math.max(freqMap.get(c), freq);

            if (i - slow + 1 - freq > k) {
                freqMap.put(s.charAt(slow), freqMap.get(s.charAt(slow))-1);
                slow++;
            }
            best = Math.max(best, i - slow + 1);
        } 
        return best;
    }
}
