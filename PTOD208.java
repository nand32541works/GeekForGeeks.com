class Solution {
    public int minSoldiers(int[] arr, int k) {
        int l=arr.length;
        int r=0;
        int[] rs= new int[l];
        int c=0;
        for (int i=0;i<l;i++){
            if(arr[i]%k==0){
                c+=1;
                rs[i]=0;
            }
            else{
                rs[i]=k-arr[i]%k;
            }
        }
        int mid=0;
        if(l%2==0){
            mid=l/2;
        }
        else{
            mid=l/2+1;
        } if(mid==c){
            r=0;
        }
        else{
            Arrays.sort(rs);
            int d=mid-c;
            int i=0;
            while(i<d){
                r+=rs[c+i];
                i++;
            }
        }
        return r;
    }
}
