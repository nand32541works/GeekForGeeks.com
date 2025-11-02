class Solution {
    public int maxEdgesToAdd(int V, int[][] edges) {
        int totalPossibleEdges = (V * (V - 1)) / 2;
        return totalPossibleEdges - edges.length;   
    }
}
