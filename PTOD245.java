class Solution {
    public int minParentheses(String s) {
        int open = 0;        
        int insertions = 0;  
        for (char c : s.toCharArray()) {
            if (c == '(') {
                open++;
            } 
            else { // c == ')'
                if (open > 0) {
                    open--; 
                } 
                else {
                    insertions++; 
                }
            }
        }
        return insertions + open;
    }
}
