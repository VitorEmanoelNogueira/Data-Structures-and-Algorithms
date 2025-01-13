from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1 


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return 0 if not node else node.height

    def get_balance_factor(self, node):
        return 0 if not node else (self.get_height(node.left) - self.get_height(node.right))

    def get_min_node(self, node):
        if node is None:
            return None
        while node.left:
            node = node.left
        return node

    # O(logn)
    def search(self, data):
        x = self.root
        while x is not None and data != x.data:
            if data < x.data:
                x = x.left
            else:
                x = x.right
        return x

    # O(logn)
    def insert(self, root, data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Update the balance factor and balance the tree
        bf = self.get_balance_factor(root)

        if bf > 1 and data < root.left.data:
            return self.right_rotate(root)
        
        if bf < -1 and data > root.right.data:
            return self.left_rotate(root)
        
        if bf > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        if bf < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

    # O(logn)
    def delete(self, root, data):
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp 
            elif not root.right:
                temp = root.left
                root = None 
                return temp 
            # find inorder successor
            temp = self.get_min_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Update the balance factor and balance the tree
        bf = self.get_balance_factor(root)

        if bf > 1 and self.get_balance_factor(root.left) >= 0:
            return self.right_rotate(root)
        
        if bf < -1 and self.get_balance_factor(root.right) <= 0:
            return self.left_rotate(root)
        
        if bf > 1 and self.get_balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        if bf < -1 and self.get_balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

    # O(1)
    def left_rotate(self, node):
        B = node.right
        Y = B.left
        
        B.left = node
        node.right = Y
        
        node.height = 1 + max(self.get_height(node.left), 
                              self.get_height(node.right))
        B.height = 1 + max(self.get_height(B.left), 
                           self.get_height(B.right))
        
        return B

    # O(1)
    def right_rotate(self, node):
        A = node.left
        Y = A.right
        
        A.right = node
        node.left = Y
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        A.height = 1 + max(self.get_height(A.left), self.get_height(A.right))
        
        return A
    
    # Level-order tree traversal
    def print_tree(self):
        if self.root:
            queue = deque()
            queue.append(self.root)

            level_order = ''
            level_order_with_details = ''

            while(queue):
                node = queue.popleft()
                level_order += f'{node.data} '
                level_order_with_details += f'{node.data}: '.ljust(5) + f'h = {self.get_height(node)}, bf = {self.get_balance_factor(node)}\n'

                # add children to queue
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            
            print('\nLevel-order traversal:')
            print(level_order)
            print(f'\nLevel-order traversal with height and balance factor:') 
            print(level_order_with_details)
        else:
            print('\nAVL tree is empty!')


def print_search_result(result):
    return result.data if result else 'not found'
            
            
if __name__ == "__main__":
    avl = AVLTree()   
    datas = [50, 25, 50, 90, 125, 83, 100]
    
    for data in datas:
        avl.root = avl.insert(avl.root, data)

    avl.print_tree()

    result = avl.search(125)
    print(f'Search for 125: {print_search_result(result)}')
    
    result = avl.search(1)
    print(f'Search for 1: {print_search_result(result)}')

    avl.root = avl.delete(avl.root, 83)
    print('\nAfter deleting 120:')
    avl.print_tree()

    avl.root = avl.delete(avl.root, 90)
    print('After deleting 10:')
    avl.print_tree()