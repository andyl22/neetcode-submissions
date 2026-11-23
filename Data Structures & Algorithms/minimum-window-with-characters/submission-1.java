public class Solution {

    public String minWindow(String s, String t) {
        if (s == null || t == null || t.isEmpty() || s.length() < t.length()) {
            return "";
        }

        // Frequency bucket for characters needed from t (ASCII)
        int[] tCount = new int[128];
        for (int i = 0; i < t.length(); i++) {
            tCount[t.charAt(i)]++;
        }

        // Frequency bucket for the current sliding window in s
        int[] windowCount = new int[128];

        int slow = 0;
        int minLen = Integer.MAX_VALUE;
        int bestStart = 0;

        for (int fast = 0; fast < s.length(); fast++) {
            // Expand window by including s.charAt(fast)
            windowCount[s.charAt(fast)]++;

            // Shrink window from the left while every required char satisfies tCount[c] <= windowCount[c]
            while (isValid(tCount, windowCount)) {
                int currentLen = fast - slow + 1;
                if (currentLen < minLen) {
                    minLen = currentLen;
                    bestStart = slow;
                }

                // Remove leftmost character and advance slow pointer
                windowCount[s.charAt(slow)]--;
                slow++;
            }
        }

        return minLen == Integer.MAX_VALUE ? "" : s.substring(bestStart, bestStart + minLen);
    }

    private boolean isValid(int[] tCount, int[] windowCount) {
        for (int c = 0; c < 128; c++) {
            if (windowCount[c] < tCount[c]) {
                return false;
            }
        }
        return true;
    }
}