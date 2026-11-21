class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();

        for (int n: nums) {
            counts.put(n, counts.getOrDefault(n,0) +1);
        }

        List<Integer> res = new ArrayList<>();
        float threshold = (float) nums.length / 3;
        for(Map.Entry<Integer, Integer> entries: counts.entrySet()) {
            Integer key = entries.getKey();
            Integer value = entries.getValue();
            if (value > threshold) {
                res.add(key);
            }
        }

        return res;
    }
}