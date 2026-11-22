class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder res = new StringBuilder();

        int l = 0;

        while (l < word1.length() && l < word2.length()) {
            res.append(word1.charAt(l)).append(word2.charAt(l));
            l++;
        }

        while (l < word1.length()) {
            res.append(word1.charAt(l));
            l++;
        }

        while (l < word2.length()) {
            res.append(word2.charAt(l));
            l++;
        }

        return res.toString();
    }
}