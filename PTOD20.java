//This code is written in java for PTOD streak

class Solution {
    Node sortedMerge(Node list1, Node list2) {
        Node dummy = new Node(0);
        Node current = dummy;
        while(list1!=null && list2!=null){
            if(list1.data <= list2.data){
                current.next = new Node(list1.data);
                current = current.next;
                list1 = list1.next;
            }
            else{
                current.next = new Node(list2.data);
                current = current.next;
                list2 = list2.next;
            }
        }
        if(list1==null && list2!=null)
        current.next = list2;
        if(list1!=null && list2==null)
        current.next = list1;
        return dummy.next;
    }
}
