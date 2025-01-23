#This code is written in Python

class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None
        current=head
        while current:
            new_node=Node(current.data)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        current = head
        copied_head = head.next
        while current:
            copied_node = current.next
            current.next = copied_node.next
            if copied_node.next:
                copied_node.next = copied_node.next.next
            current = current.next
        return copied_head
