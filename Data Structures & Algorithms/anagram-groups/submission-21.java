class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        Map<String,List<String>> bucketMap = new HashMap<>();

        for(String s: strs) {
            char[] sArray = s.toCharArray();
            Arrays.sort(sArray);
            String key = String.valueOf(sArray);
            bucketMap.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        for(List<String> v: bucketMap.values()) res.add(v);
        return res;
    }
}
