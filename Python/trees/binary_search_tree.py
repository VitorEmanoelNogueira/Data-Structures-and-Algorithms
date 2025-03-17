class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data in the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    # Depth First Traversal  
    def in_order_traversal(self):
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #visit base node
        elements.append(self.data)
        
        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)
        
        return elements
    
    def pre_order_traversal(self):
        elements = [self.data]


        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements
    
    #Breadth First Traversal
    def breadth_first_traversal(self):
        elements = []
        queue = [self]
        
        while (len(queue) > 0):
            curr = queue.pop(0)
            elements.append(curr.data)
            
            if(curr.left is not None):
                queue.append(curr.left)
            
            if (curr.right is not None):
                queue.append(curr.right)
        
        return elements
                 
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            #val  might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False


        if val > self.data:
            #val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def find_min(self):
        # vá até a esquerda até achar o último elemento
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        # vá até a esquerda até achar o último elemento
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            # substitutes node with two children nodes with the min of the right subtree
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

            # substitues node with two children nodes with the max value of the left subtree
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self
    
    def calculate_sum(self):
        elements = 0

        #visit left tree
        if self.left:
            elements += self.left.calculate_sum()

        #visit base node
        elements += self.data
        
        #visit right tree
        if self.right:
            elements += self.right.calculate_sum()

        return elements
        


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers = [17, 4, 3, 20, 9, 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.breadth_first_traversal())
    print(numbers_tree.search(18))
    print(numbers_tree.search(25))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
    
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(23)
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(17)
    print(numbers_tree.in_order_traversal())
    

    print(numbers_tree.calculate_sum())


