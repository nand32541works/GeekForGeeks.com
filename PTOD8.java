//This is the code for today's geekforgeeks PTOD streak

class Solution {
    static int countTriangles(int arr[]) {
        Arrays.sort(arr);
        int n=arr.length;
        int cnt=0;
        for(int i=2;i<n;i++){
             int j=0;
             int k=i-1;
             while(j < k){
                int sum=arr[j]+arr[k];
                if(sum > arr[i]){
                    cnt+=k-j;
                    k--;
                }
                else{
                   j++;
                }
             }
        }
        return cnt;
    }
}
