/*
class Node{
    int data;
    Node left;
    Node right;
    Node(int data){
        this.data = data;
        left=null;
        right=null;
    }
} */
class Solution{
    static int sum =0;
    public static void inorder(Node root){
        if(root == null){
           return;
        }
        inorder(root.right);
        int x = root.data;
        root.data = sum;
        sum += x;
        inorder(root.left);
    }
    public static void transformTree (Node root){
        sum = 0;
        inorder(root);
    }
}
