#creating binary tree


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_rec(self.root, value)

    def insert_rec(self, current_node, value):
        if current_node.left is None:
            current_node.left = Node(value)
        elif current_node.right is None:
            current_node.right = Node(value)
        else: 
            if current_node.left.left is None or current_node.left.right is None:
                self.insert_rec(current_node.left,value)
            else:
                self.insert_rec(current_node.right, value)   

    def printTree(self, current_node=None, level = 0):
        if current_node is None:
            current_node = self.root
        print(' ' * level + str(current_node.value))
        if current_node.left:
            self.printTree(current_node.left, level+1)
        if current_node.right:
            self.printTree(current_node.right, level+1)

tree = Tree()

ls = [1,2,3,4,5,6,7]
for i in ls:
    tree.insert(i)
tree.printTree()         
