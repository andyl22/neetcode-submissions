class Solution {
    public boolean checkInclusion(String s1, String s2) {
        char[] s1Array = s1.toCharArray();
        Arrays.sort(s1Array);
        String sortedS1 = String.valueOf(s1Array);
        int slow = 0;

        for(int fast = 0; fast < s2.length(); fast++) {
            if(fast-slow+1 > s1.length()) {
                slow++;
            }
            char[] s2Array = s2.substring(slow, fast+1).toCharArray();
            Arrays.sort(s2Array);
            String sortedS2 = String.valueOf(s2Array);
            if (sortedS1.equals(sortedS2)) {
                return true;
            }
        }

        return false;
    }
}
