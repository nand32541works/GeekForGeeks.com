//This code is written in java

class Solution {
    private int maxDiameter = 0;
    int diameter(Node root) {
        height(root);
        return maxDiameter;
    }
    private int height(Node node) {
        if (node == null) return 0;
        int leftHeight = height(node.left);
        int rightHeight = height(node.right);
        maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight);
        return 1 + Math.max(leftHeight, rightHeight);
    }
}
