class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<List<Integer>, List<String>> countMap = new HashMap<>();

        for (String word : strs) {
            int[] count = new int[26];
            for (int i = 0; i < word.length(); i++) {
                count[word.charAt(i) - 'a']++;
            }

            List<Integer> key = new ArrayList<>(26);
            for (int freq : count) {
                key.add(freq);
            }

            countMap.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
        }

        return new ArrayList<>(countMap.values());
    }
}