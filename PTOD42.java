//This code is written in java

class Solution {
    boolean bstCheck(Node root,int min,int max){
        if(root == null) return true;
        if(root.data <= min || root.data >= max) return false;
        return bstCheck(root.left,min,root.data) && bstCheck(root.right,root.data,max);
    }
    boolean isBST(Node root) {
      return bstCheck(root,Integer.MIN_VALUE,Integer.MAX_VALUE);
    }
}
