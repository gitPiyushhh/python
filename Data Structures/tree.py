class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
    

class BinaryTree:
    def __init__(self):
        self.root = None
    
if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)

    print(tree.root.data)