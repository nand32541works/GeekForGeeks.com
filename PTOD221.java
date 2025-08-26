class Solution {
    public boolean isSubSeq(String s1, String s2) {
        int n=s1.length(), m=s2.length();
        if(n>m)return false;
        int i=0;
        for(int j=0;j<m;j++){
            if(s2.charAt(j)==s1.charAt(i))i++;
            if(i>=n)return true;
        }
        return false;
    }
};
