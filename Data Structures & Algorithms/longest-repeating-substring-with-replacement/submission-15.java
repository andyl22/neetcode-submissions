class Solution {
    public int characterReplacement(String s, int k) {
        int best = 0;
        int slow = 0;
        int freq = 0;
        Map<Character, Integer> freqMap = new HashMap<>();

        for (int fast = 0; fast < s.length(); fast++) {
            freqMap.merge(s.charAt(fast), 1, Integer::sum);
            freq = Math.max(freqMap.get(s.charAt(fast)), freq);
            if(fast - slow + 1 - freq> k) {
                freqMap.put(s.charAt(slow), freqMap.get(s.charAt(slow))-1);
                slow++;
            }
            best = Math.max(fast - slow + 1, best);
        }
        
        return best;
    }
}
