class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder res = new StringBuilder(word1.length() + word2.length());
        int l = 0;

        while (l < word1.length() && l < word2.length()) {
            res.append(word1.charAt(l)).append(word2.charAt(l));
            l++;
        }

        res.append(word1.substring(l)).append(word2.substring(l));
        return res.toString();
    }
}