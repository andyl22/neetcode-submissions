class Solution {

    public String encode(List<String> strs) {
        StringBuilder stringBuilder = new StringBuilder();
        for(String s: strs) {
            stringBuilder.append(s.length()).append("#").append(s);
        }
        return stringBuilder.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int l = 0;
        while (l < str.length()) {
            int j = l;
            while (str.charAt(j) != '#') {
                j++;
            }
            int length = Integer.parseInt(str.substring(l, j));
            j++;
            res.add(str.substring(j, j+length));
            l = j + length;
        }
        return res;
    }
}
