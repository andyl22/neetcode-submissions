class Solution {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Integer> remainderMap = new HashMap<>();

        for(int i = 0; i <numbers.length; i++) {
            int remainder = target - numbers[i];
            if(remainderMap.containsKey(remainder)) return new int[]{remainderMap.get(remainder)+1,i+1};
            remainderMap.put(numbers[i],i);
        }

        return new int[]{};
    }
}
