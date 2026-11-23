class KthLargest {
    private PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    private int maxSize;
    public KthLargest(int k, int[] nums) {
        maxSize = k;
        for(int n: nums) {
            minHeap.offer(n);
            evictIfNeeded();
        }
    }
    
    public int add(int val) {
        minHeap.offer(val);
        evictIfNeeded();
        return minHeap.peek();
    }

    private void evictIfNeeded() { 
        if (minHeap.size() > maxSize) {
            minHeap.poll();
        }
    }
}
