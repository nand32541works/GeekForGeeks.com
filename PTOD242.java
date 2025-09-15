class Solution {
    public int evaluatePostfix(String[] arr) {
        Stack<Integer> st = new Stack<>();
        for (String token : arr) {
            if (Character.isDigit(token.charAt(0)) ||
                (token.length() > 1 && token.charAt(0) == '-')) {
                st.push(Integer.parseInt(token));
            } else {
                int val1 = st.pop();
                int val2 = st.pop();

                if (token.equals("+"))
                    st.push(val2 + val1);
                else if (token.equals("-"))
                    st.push(val2 - val1);
                else if (token.equals("*"))
                    st.push(val2 * val1);
                else if (token.equals("/")) {
                    if (val2 * val1 < 0 && val2 % val1 != 0)
                        st.push(val2 / val1 - 1);
                    else
                        st.push(val2 / val1);
                } 
                else if (token.equals("^"))
                    st.push((int)Math.pow(val2, val1));
            }
        }
        return st.pop();
    }
}
