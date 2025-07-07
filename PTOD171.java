class Solution {
    public ArrayList<Integer> nextLargerElement(int[] arr) {
        Stack<Integer>st=new Stack<>();
        ArrayList<Integer>list=new ArrayList<>();
        int j=0;
        int n=arr.length;
        for(int i=n-1;i>=0;i--){
            if(!st.isEmpty()){
                if(st.peek()>arr[i]){
                    list.add(0,st.peek());
                }
                else{
                    while(!st.isEmpty()&&arr[i]>=st.peek())st.pop();
                    if(!st.isEmpty())list.add(0,st.peek());
                }
            }
            if(st.isEmpty()){
                while(st.isEmpty()&&j<i&&arr[j]<=arr[i])j++;
                if(st.isEmpty()&&j<i){
                    list.add(0,arr[j]);
                }
                else if(st.isEmpty()&&j>=i)list.add(0,-1);
            }
            st.push(arr[i]);
        }
        return list;
    }
}
