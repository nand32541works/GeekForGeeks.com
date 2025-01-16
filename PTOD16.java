//This is the code for today's streak

class Solution {
    public int maxLen(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 0) {
                arr[i] = -1;
            }
        }
        HashMap<Integer, Integer> sumIndexMap = new HashMap<>();
        sumIndexMap.put(0, -1); 
        int maxLength = 0;
        int cumulativeSum = 0;
        for (int i = 0; i < arr.length; i++) {
            cumulativeSum += arr[i];
            if (sumIndexMap.containsKey(cumulativeSum)) {
                int length = i - sumIndexMap.get(cumulativeSum);
                maxLength = Math.max(maxLength, length);
            } 
            else {
                sumIndexMap.put(cumulativeSum, i);
            }
        }
        return maxLength;
    }
}
