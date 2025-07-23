class Solution {
    public int subarraySum(int[] arr) {
        int n=arr.length;
        int sum = 0;
        for (int i = 0; i < n; i++){
            int cnt=(i+1)*(n-i);
            sum+=arr[i]*cnt;  
        } 
        return sum;
    }
}
