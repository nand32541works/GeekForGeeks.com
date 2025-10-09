/*
class Node {
    int data;
    Node left,right;
    Node(int d)
    {
        data=d;
        left=right=null;
    }
}
*/
class Solution {
    ArrayList<Integer> zigZagTraversal(Node root) {
        Stack<Node> stack = new Stack<>();
        stack.push(root);
        ArrayList<Integer> ans = new ArrayList<>();
        int level = 0;
        while(!stack.isEmpty()) {
            int size = stack.size();
            Stack<Node> stack2 = new Stack<>();
            for(int i=0; i<size ; i++) {
                Node node = stack.pop();
                ans.add(node.data);
                if(level%2 == 0) {
                    if(node.left!=null) stack2.add(node.left);
                    if(node.right!=null) stack2.add(node.right);
                } 
                else {
                    if(node.right!=null) stack2.add(node.right);
                    if(node.left!=null) stack2.add(node.left);
                }
            }
            stack = stack2;
            level++;
        }
        return ans;
    }
}
