class Solution {
    public String mergeAlternately(String word1, String word2) {
        int l = 0;
        StringBuilder stringBuilder = new StringBuilder();
        while (l < word1.length() && l < word2.length()) {
            stringBuilder.append(word1.charAt(l)).append(word2.charAt(l));
            l += 1;
        }
        while (l<word1.length()) {
            stringBuilder.append(word1.charAt(l));
            l += 1;
        }

        while (l < word2.length()) {
            stringBuilder.append(word2.charAt(l));
            l += 1;
        }
        return stringBuilder.toString();
    }
}