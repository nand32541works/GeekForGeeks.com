class Solution {
    public static void reverseArray(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
    public static void rotateDeque(Deque<Integer> dq, int type, int k) {
        int n = dq.size();
        if (n == 0) return;
        k = k % n;
        if (k == 0) return;
        Integer[] arrObj = dq.toArray(new Integer[0]);
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = arrObj[i];
        if (type == 1) {
            reverseArray(arr, 0, n - 1);
            reverseArray(arr, 0, k - 1);
            reverseArray(arr, k, n - 1);
        } 
        else if (type == 2) {
            reverseArray(arr, 0, k - 1);
            reverseArray(arr, k, n - 1);
            reverseArray(arr, 0, n - 1);
        }
        dq.clear();
        for (int val : arr) dq.add(val);
    }
}
