class Solution {
    public static boolean isSymmetric(Node root) {
        if(root==null) return true;
        return help(root.left,root.right);
    }
    static boolean help(Node l,Node r){
        if(l==null && r==null) return true;
        if(l==null || r==null) return false;
        return (l.data==r.data)&&help(l.left,r.right)&&help(l.right,r.left);
    }
}
