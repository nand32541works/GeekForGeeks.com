//This code is written in JAVA

class Solution {
    public static void removeLoop(Node head) {
        if(head == null || head.next == null) return;
        Node fast= head;
        Node slow = head;
        while(fast!=null && fast.next !=null){
           fast = fast.next.next;
           slow = slow.next;
           if(slow == fast){
               Node entry= head;
               while(slow != entry){
                   slow=slow.next ;
                   entry= entry.next;
               }
               Node loop = entry;
               while(loop.next != entry){
                   loop = loop.next;
               }
               loop.next = null;
           }
        }
    }
}
