class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<List<Integer>> freq = new ArrayList<>();
        Map<Integer, Integer> freqMap = new HashMap<>();

        for (int i = 0; i < nums.length+1; i++) {
            freq.add(i,new ArrayList<>());
        }

        for (int n: nums) {
            freqMap.put(n, freqMap.getOrDefault(n, 0) + 1);
        }

        for(Map.Entry<Integer, Integer> entry: freqMap.entrySet()) {
            int frequency = entry.getValue();
            int key = entry.getKey();
            freq.get(frequency).add(key);
        }

        int[] res = new int[k];

        int index = 0;
        for(int i = freq.size()-1; i > 0; i--) {
            for(int j = 0; j < freq.get(i).size(); j++) {
                if (index == k) {
                    return res;
                }
                res[index++] = (freq.get(i).get(j));
            }
        }

        return res;
    }
}
