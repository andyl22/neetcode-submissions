class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap<>();

        for (String s: strs) {
            char[] cArray = s.toCharArray();
            Arrays.sort(cArray);
            String key = new String(cArray);
            anagrams.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(anagrams.values());
    }
}
