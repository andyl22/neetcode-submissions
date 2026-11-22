class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        Deque<Double> times = new ArrayDeque<>();

        int[][] cars = new int[position.length][2];
        for(int i = 0; i < position.length; i++) {
            cars[i][0] = position[i];
            cars[i][1] = speed[i];
        }

        Arrays.sort(cars, (a,b) -> Integer.compare(b[0],a[0]));

        for(int[] c: cars) {
            double time = (double) (target-c[0]) / c[1];
            if (times.size() > 0 && time <= times.peek()) {
                continue;
            } else {
                times.push(time);
            }
        }

        return times.size();
    }
}
