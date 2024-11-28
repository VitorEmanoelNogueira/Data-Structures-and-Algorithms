class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def print_forward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + " -> "
            itr = itr.next
        
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.get_last_node()
        llstr = ''
        while itr:
            llstr += str(itr.data) + " ->  "
            itr = itr.prev

        print(f"Reverse Linked List: {llstr}")

    def get_last_node(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        return itr
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count


    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None, itr)
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


# Iterative -> T - O(n); M - O(1)
def reverse_linked_list_i(head: Node) -> Node:
    prev = None
    curr = head
    
    while curr:
        nxt = curr.next
        curr.next = prev
        curr.prev = nxt
        prev = curr
        curr = nxt

    return prev

def reverse_linked_list_r(head: Node) -> Node:
    if not head: 
        return None

    newHead = head
    if head.next is not None:
        newHead = reverse_linked_list_r(head.next)
        head.next.prev = head.next.next
        head.next.next = head
    head.next = None

    return newHead


if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    # ll.head = reverse_linked_list_i(ll.head)
    ll.head = reverse_linked_list_r(ll.head) 
    ll.print_forward()