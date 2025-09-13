class Solution {
    public int startStation(int[] gas, int[] cost) {
        int n = gas.length;
        int totalGas = 0;
        int currGas = 0;
        int startIdx = 0;
        for (int i = 0; i < n; i++) {
            currGas += gas[i] - cost[i];
            totalGas += gas[i] - cost[i];
            if (currGas < 0) {
                currGas = 0;
                startIdx = i + 1;
            }
        }
        if (totalGas < 0) return -1;
        return startIdx;
    }
}
