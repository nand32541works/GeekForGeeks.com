class Solution {
    public Node segregate(Node head) {
        int count0=0,count1=1,count2=2;
        Node temp=head;
        while(temp!=null){
            if(temp.data==0)count0++;
            else if(temp.data==1)count1++;
            else count2++;
            temp=temp.next;
        }
        temp=head;
        while(count0>0){
            temp.data=0;
            temp=temp.next;
            count0--;
        }
        while(count1>1){
            temp.data=1;
            temp=temp.next;
            count1--;
        }
        
        while(count2>2){
            temp.data=2;
            temp=temp.next;
            count2--;
        }
        return head;
    }
}
