class Solution {
    public static int minCost(int[] arr) {
        int minCost = 0;
        int n = arr.length;
        PriorityQueue<Integer> pq = new PriorityQueue<>();  
        for(int i = 0; i<n;i++){
            pq.add(arr[i]);
        }
        while(pq.size()>1){
            int first = pq.poll();  
            int second = pq.poll();  
            int sum = first+second;
            minCost += sum;  
            pq.add(sum);  
        }
        return minCost;
    }
}
