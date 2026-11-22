class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();
        if (m > n) {
            return false;
        }

        int[] s1Count = new int[26];
        int[] s2Count = new int[26];

        // Seed the initial window of size m
        for (int i = 0; i < m; i++) {
            s1Count[s1.charAt(i) - 'a']++;
            s2Count[s2.charAt(i) - 'a']++;
        }

        if (Arrays.equals(s1Count, s2Count)) {
            return true;
        }

        // Slide the window across s2: add right (i), remove left (i - m)
        for (int i = m; i < n; i++) {
            s2Count[s2.charAt(i) - 'a']++;
            s2Count[s2.charAt(i - m) - 'a']--;

            if (Arrays.equals(s1Count, s2Count)) {
                return true;
            }
        }

        return false;
    }
}