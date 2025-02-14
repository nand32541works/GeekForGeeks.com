//This code is in java

class Solution {
    Node prev;
    Node first;
    Node mid;
    Node last;
    void inorder(Node root){
        if(root==null) return;
        inorder(root.left);
        if(root.data<prev.data){
            if(first==null){
                first=prev;
                mid=root;
            }
            else{
                last=root;
            }
        }
        prev=root;
        
        inorder(root.right);
    }
    void correctBST(Node root) {
        first=mid=last=null;
        prev=new Node(Integer.MIN_VALUE);
        inorder(root);
        if(first!=null && last!=null){
            int temp=first.data;
            first.data=last.data;
            last.data=temp;
        }
        else{
            int temp=first.data;
            first.data=mid.data;
            mid.data=temp;
        }
    }
}
