class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        Deque<Double> times = new ArrayDeque<>();

        int n = position.length;
        int[][] cars = new int[n][2];

        for (int i = 0; i < n; i++) {
            cars[i][0] = position[i];
            cars[i][1] = speed[i];
        }

        Arrays.sort(cars, (a, b) -> Integer.compare(b[0], a[0]));
        for(int[] c: cars) {
            double time = (double) (target - c[0]) / c[1];
            if(times.size() > 0 && times.peek() >= time) {
                continue;
            } else {
                times.push(time);
            }
        } 

        return times.size();
    }
}
