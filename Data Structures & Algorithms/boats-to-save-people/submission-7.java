class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);

        int l = 0;
        int r = people.length-1;
        int boats = 0;

        while (l <= r) {
            int total = people[l] + people[r];
            if (total > limit) {
                r--;
            } else {
                l++;
                r--;
            }
            boats++;
        }
        return boats;
    }
}