
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();
        if (m > n) {
            return false;
        }

        int[] s1Count = new int[26];
        for (int i = 0; i < m; i++) {
            s1Count[s1.charAt(i) - 'a']++;
        }

        // Try every possible starting index for a substring of length m in s2
        for (int start = 0; start <= n - m; start++) {
            int[] s2Count = new int[26];
            for (int j = start; j < start + m; j++) {
                s2Count[s2.charAt(j) - 'a']++;
            }

            if (Arrays.equals(s1Count, s2Count)) {
                return true;
            }
        }

        return false;
    }
}