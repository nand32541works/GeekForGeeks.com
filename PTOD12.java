//This file is written in JAVA

class Solution {
    public int maxWater(int arr[]) {
        int n=arr.length;
        int[] lft=new int[n];
        int[] rgt=new int[n];
        lft[0]=arr[0];
        for(int i=1;i<n;i++){
            lft[i]=Math.max(arr[i],lft[i-1]);
        }
        rgt[n-1]=arr[n-1];
        for(int i=n-2;i>=0;i--){
            rgt[i]=Math.max(arr[i],rgt[i+1]);
        }
        int res=0;
        for(int i=0;i<n;i++){
            int water=Math.min(lft[i],rgt[i]);
            res+=water-arr[i];
        }
        return res;
    }
}
