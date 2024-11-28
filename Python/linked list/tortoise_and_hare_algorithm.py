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


def create_cycle(head: Node, cycle_value) -> Node:
    curr = head
    cycle_node = None
    while curr.next:
        if curr.data == cycle_value:
            cycle_node = curr
        curr = curr.next
    curr.next = cycle_node
    
    return cycle_node

def detect_cycle(head: Node) -> Node:
    slow = fast = head
    met = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow ==fast:
            met = True
            break
    if not met:
        return None
    else:
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print()
    create_cycle(ll.head, 6)
    start_of_cycle = detect_cycle(ll.head)

    if start_of_cycle:
        print(f"Cycle detected starting in the node with value: {start_of_cycle.data}")
    else:
        print("No cycle detected")

    