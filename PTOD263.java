/*
class Node {
    int data;
    Node left, right;
    Node(int val){
        data = val;
        left = right = null;
    }
}
*/

import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> postOrder(Node root) {
        ArrayList<Integer> ans = new ArrayList<>();
        if (root == null)
            return ans;
        ArrayList<Integer> left = postOrder(root.left);
        ArrayList<Integer> right = postOrder(root.right);
        ans.addAll(left);
        ans.addAll(right);
        ans.add(root.data);
        return ans;
    }
}
