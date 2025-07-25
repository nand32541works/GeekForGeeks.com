class Solution {
    public int maxCircularSum(int arr[]) {
        int n = arr.length;
        int max_kadane = kadane(arr);
        int total_sum = 0;
        for (int i = 0; i < n; i++) {
            total_sum += arr[i];
            arr[i] = -arr[i]; 
        }
        int max_inverse_kadane = kadane(arr); 
        int max_circular = total_sum + max_inverse_kadane;
        if (max_circular == 0)
            return max_kadane;
        return Math.max(max_kadane, max_circular);
    }
    private int kadane(int[] arr) {
        int max_so_far = arr[0];
        int current_max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            current_max = Math.max(arr[i], current_max + arr[i]);
            max_so_far = Math.max(max_so_far, current_max);
        }
        return max_so_far;
    }
}
