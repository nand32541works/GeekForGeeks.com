class Solution {
    public TreeMap<Integer, int[]> mp = new TreeMap<>();
    public void insert(int val) {
        Map.Entry<Integer, int[]> it = mp.ceilingEntry(val);
        int len = 1;
        int sum = val;
        Map.Entry<Integer, int[]> prev = mp.lowerEntry(val);
        if (prev != null) 
        {
            len = prev.getValue()[0] + 1;
            sum = prev.getValue()[1] + val;
        }
        List<Integer> toerase = new ArrayList<>();
        while (it != null) 
        {
            if (it.getValue()[0] > len) break;
            toerase.add(it.getKey());
            it = mp.higherEntry(it.getKey());
        }
        for (int key : toerase) {
            mp.remove(key);
        }
        mp.put(val, new int[] {len, sum});
    }
    public int nonLisMaxSum(int[] arr) {
        mp.clear();
        for (int val : arr) 
        {
            insert(val);
        }
        int[] last = mp.lastEntry().getValue();
        int totalSum = Arrays.stream(arr).sum();
        int lisSum = last[1];
        return totalSum - lisSum;
    }
}
