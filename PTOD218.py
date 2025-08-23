class Solution {
    public int findPages(int[] arr, int k) {
        int n = arr.length;
        if (k > n) return -1;
        int low = Integer.MIN_VALUE;
        int high = 0;
        for (int i = 0; i < n; i++) 
        {
            high += arr[i];                 
            low = Math.max(low, arr[i]);    
        }
        int result = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;  
            int students = 1;                  
            int pageSum = 0;                   
            boolean possible = true;           
            for (int i = 0; i < n; i++) {
                if (arr[i] > mid) {
                    possible = false;  
                    break;
                }

                if (pageSum + arr[i] > mid) {
                    students++;             
                    pageSum = arr[i];       
                } 
                else {
                    pageSum += arr[i];      
                }
            }
            if (possible && students <= k) {
                result = mid;          
                high = mid - 1;
            } 
            else {
                low = mid + 1;        
            }
        }
        return result;
    }
}
