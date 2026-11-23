class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int n : nums) {
            counter.merge(n, 1, Integer::sum);
        }

        PriorityQueue<Integer> topK = new PriorityQueue<>(
            Comparator.comparingInt(counter::get)
        );
        for (int n : counter.keySet()) {
            topK.offer(n);
            if (topK.size() > k) {
                topK.poll();
            }
        }

        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = topK.poll();
        }
        return res;
    }
}