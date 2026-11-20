class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) { return false; }
        Map<Character, Integer> cMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            Character sChar = s.charAt(i);
            Character tChar = t.charAt(i);
            cMap.put(sChar, cMap.getOrDefault(sChar, 0) + 1);
            cMap.put(tChar, cMap.getOrDefault(tChar, 0) - 1);
        }

        for (int count: cMap.values()) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }
}
