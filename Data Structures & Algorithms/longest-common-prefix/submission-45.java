class Solution {
    public String longestCommonPrefix(String[] strs) {
        /*
        b a t
        b a g
        b a n k
        b a n d
        */
        StringBuilder prefix = new StringBuilder();

        for(int i = 0; i < strs[0].length(); i++) {
            Character s = strs[0].charAt(i);
            for(String str: strs) {
                if(i==str.length() || str.charAt(i) != s) return prefix.toString();
            }
            prefix.append(s);
        }

        return prefix.toString();

    }
}