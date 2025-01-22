//THIS CODE IS IN JAVA

class Solution {
    static Node addTwoLists(Node num1, Node num2) {
    num1 = reverse(num1);
    num2 = reverse(num2);
    Node first = num1, second = num2;
    Node result = new Node(0);
    Node curr = result;
    int carry = 0;
    while(first != null || second != null){
        int x = (first != null)? first.data: 0;
        int y = (second != null)? second.data: 0;
        int sum = x + y + carry;
        carry = sum/10;
        curr.next = new Node(sum % 10);
        curr = curr.next;
        if(first != null) first = first.next;
        if(second != null) second = second.next;
    }
    if(carry > 0) curr.next = new Node(carry);
    result = reverse(result.next);
    while(result.next != null && result.data == 0) result = result.next;
    return result;
    }
    static Node reverse(Node head){
    Node prev = null, curr = head;
    while(curr != null){
        Node next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
    }
}
