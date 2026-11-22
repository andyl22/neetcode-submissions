class Solution {
    public int calPoints(String[] operations) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < operations.length; i++) {
            String o = operations[i];
            switch (o) {
                case "+" -> {
                    int n1 = stack.pop();
                    int n2 = stack.pop();
                    stack.push(n2);
                    stack.push(n1);
                    stack.push(n2+n1);
                }
                case "D" -> stack.push(stack.peek() * 2);
                case "C" -> stack.pop();
                default -> stack.push(Integer.parseInt(o));
            }
        }
        int sum = 0;
        for (int score : stack) {
            sum += score;
        }
        return sum;
    }
}