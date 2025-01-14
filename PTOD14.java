//This is a code in java for today's streak

class Solution {
    public static int findEquilibrium(int arr[]) {
        int[] pref=new int[arr.length];
        pref[0]=arr[0];
        int n=arr.length;
        for(int i=1;i<n;i++)pref[i]=pref[i-1]+arr[i];
        for(int i=1;i<n-1;i++)if(pref[i-1]==pref[n-1]-pref[i])return i;
        return -1;
    }
}
