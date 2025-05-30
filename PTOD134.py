class Solution {
    public int findMaxFork(Node root, int k) {
        int ans[]=new int[1];
        rec(root,k,new int[]{Integer.MAX_VALUE},ans);
        return ans[0]==0?-1:ans[0];
    }
    private void rec(Node root,int k,int[] dis,int[] nei){
        if(root==null) return;
        if(k>=root.data && k-root.data<dis[0]){
            dis[0]=k-root.data;
            nei[0]=root.data;
        }
        rec(root.left,k,dis,nei);
        rec(root.right,k,dis,nei);
    }
}
