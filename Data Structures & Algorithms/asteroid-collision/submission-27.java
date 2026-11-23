class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> stack = new ArrayDeque<>();

        outer:
        for (int a : asteroids) {
            while (!stack.isEmpty() && a < 0 && stack.peek() > 0) {
                int top = stack.peek();
                if (top < -a) {
                    stack.pop(); // current right-mover explodes; keep checking
                } else if (top == -a) {
                    stack.pop(); // both explode
                    continue outer;
                } else {
                    continue outer; // incoming left-mover explodes
                }
            }
            stack.push(a);
        }

        int[] res = new int[stack.size()];
        for (int i = res.length - 1; i >= 0; i--) {
            res[i] = stack.pop();
        }
        return res;
    }
}