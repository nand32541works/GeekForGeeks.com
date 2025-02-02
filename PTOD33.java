//This code is in java

class Solution {
    public ArrayList<ArrayList<Integer>> levelOrder(Node root) {
        ArrayList<ArrayList<Integer>> l = new ArrayList<>();
        if (root == null) 
            return l;
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            int size = q.size();
            ArrayList<Integer> ll = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                Node temp = q.poll();
                ll.add(temp.data);
                if (temp.left != null) q.add(temp.left);
                if (temp.right != null) q.add(temp.right);
            }
            l.add(ll);
        }
        return l;
    }
}
