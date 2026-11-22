
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();
        if (m > n) {
            return false;
        }

        int[] s1Count = new int[26];
        int[] s2Count = new int[26];

        for (int i = 0; i < m; i++) {
            s1Count[s1.charAt(i) - 'a']++;
        }

        int slow = 0;
        // Try every possible starting index for a substring of length m in s2
        for (int i = 0; i < s2.length(); i++) {
            int index = s2.charAt(i) - 'a';
            s2Count[index]++;

            if (i - slow + 1 > s1.length()) {
                int slowIndex = s2.charAt(slow) - 'a';
                s2Count[slowIndex]--;
                slow++;
            }

            if (Arrays.equals(s1Count, s2Count)) {
                return true;
            }
        }

        return false;
    }
}