//This code is written in java

class Solution {
    ArrayList<Integer>arr=new ArrayList<>();
    public void BST(Node root){
        if(root!=null){
        arr.add(root.data);
        BST(root.left);
        BST(root.right);
        }
        else
        return;
    }
    public int kthSmallest(Node root, int k) {
        BST(root);
        Collections.sort(arr);
        if(k>arr.size())
        return -1;
        return arr.get(k-1);
    }
}
