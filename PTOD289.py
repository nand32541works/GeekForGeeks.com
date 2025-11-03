class Solution {
    int minCost(int[] h) {
        int n = h.length;
        int pre1 = 0;
        int pre2 = 0;
        
        for (int i = 1; i < n; i++) {
            int ls = pre1 + Math.abs(h[i] - h[i - 1]);
            int rs = Integer.MAX_VALUE;
            
            if (i > 1) 
            rs = pre2 + Math.abs(h[i - 2] - h[i]);
            
            int curr = Math.min(ls, rs);
            pre2 = pre1;
            pre1 = curr;
        }
        return pre1;
    }
}
