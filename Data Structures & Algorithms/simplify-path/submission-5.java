class Solution {
    public String simplifyPath(String path) {
        String[] splitPaths = path.split("/");
        Deque<String> paths = new ArrayDeque<>();

        for(String s: splitPaths) {
            if (s.equals("..")) {
                if (!paths.isEmpty()) paths.pollLast();
            } else if (!s.equals(".") && !s.equals("")) {
                paths.offerLast(s);
            }
        }

        return "/" + String.join("/", paths);
    }
}