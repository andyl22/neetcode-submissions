class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] s1Count = new int[26];
        int[] s2Count = new int[26];
        int matches = 0;
        int slow = 0;

        for (int i = 0; i < s1.length(); i++) {
            s1Count[s1.charAt(i) - 'a']++;
        }

        for(int i = 0; i < s1Count.length; i++) {
            if(s1Count[i] == s2Count[i]) {
                matches++;
            }
        }

        for(int i = 0; i < s2.length(); i++) {
            int index = s2.charAt(i) - 'a';
            if (s2Count[index] == s1Count[index]-1) {
                matches++;
            }
            if (s2Count[index] == s1Count[index]) {
                matches--;
            }
            s2Count[index]++;
            
            if(i - slow + 1 > s1.length()) {
                int slowIndex = s2.charAt(slow) - 'a';
                if (s2Count[slowIndex] == s1Count[slowIndex]) {
                    matches--;
                }
                if (s2Count[slowIndex] == s1Count[slowIndex]+1) {
                    matches++;
                }
                s2Count[slowIndex]--;
                slow++;
            }

            
            if (i - slow + 1 == s1.length() && matches==26) {
                return true;
            }
        }
        return false;


    }
}
