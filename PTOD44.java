//This code is written in java

class Solution {
    boolean findTarget(Node root, int target) {
        ArrayList<Integer> inorder = new ArrayList<>();
        inOrder(root, inorder);
        int start = 0;
        int end = inorder.size() - 1;
        while (start < end) {
            int sum = inorder.get(start) + inorder.get(end);
            if (sum > target) end--;
            else if (sum < target) start++;
            else return true;
        }
        return false;
    }
    void inOrder(Node root, ArrayList<Integer> list) {
        if (root.left != null) inOrder(root.left, list);
        list.add(root.data);
        if (root.right != null) inOrder(root.right, list);
    }
}
