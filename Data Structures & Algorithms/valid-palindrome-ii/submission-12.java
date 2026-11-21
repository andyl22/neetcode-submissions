class Solution {
    public boolean validPalindrome(String s) {
        
        int l = 0;
        int r = s.length()-1;

        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return validPalindrome(s.substring(l,r), false) || validPalindrome(s.substring(l+1,r+1), false);
            }
            l += 1;
            r -= 1;
        }

        return true;
    }

    private boolean validPalindrome(String s, boolean alive) {
        
        int l = 0;
        int r = s.length()-1;

        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return false;
            }
            l += 1;
            r -= 1;
        }

        return true;
    }
}