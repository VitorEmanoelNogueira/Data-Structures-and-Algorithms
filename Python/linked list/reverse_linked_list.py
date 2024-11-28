class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + " -> "
            itr = itr.next
        
        print(llstr)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)   

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
        prev = curr
        curr = nxt

    return prev

# Recursive -> T - O(n); M - O(n)
def reverse_linked_list_r(head: Node) -> Node:
    if not head: 
        return None

    newHead = head
    if head.next is not None:
        newHead = reverse_linked_list_r(head.next)
        head.next.next = head
    head.next = None

    return newHead



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    # ll.head = reverse_linked_list_i(ll.head)
    ll.head = reverse_linked_list_r(ll.head)
    ll.print()
