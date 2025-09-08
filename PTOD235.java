class Solution {
    public int assignHole(int[] mices, int[] holes) {
        Arrays.sort(mices);
        Arrays.sort(holes);
        int n = mices.length;
        int max = 0;
        for (int i = 0; i < n; i++)
            if (max < Math.abs(mices[i] - holes[i]))
                max = Math.abs(mices[i] - holes[i]);
        return Math.abs(max);
    }
};
