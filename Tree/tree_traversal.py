
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def get_root(self):
        return self.root
    
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
            if self.height(current_node.left) <= self.height(current_node.right):
                self.insert_rec(current_node.left, value)
            else:
                self.insert_rec(current_node.right, value)   

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def printTree(self, current_node=None, level = 0):
        if current_node is None:
            current_node = self.root
        print(' ' * level + str(current_node.value))
        if current_node.left:
            self.printTree(current_node.left, level+1)
        if current_node.right:
            self.printTree(current_node.right, level+1)


  
    #          1
    #       /     \
    #      2       3
    #    /    \
    #   4      5
    #        /    \
    #       6      7


# Inorder Traversal
# 1. Traverse the left subtree i.e. call Inorder(left-subtree)
# 2. Visit the Node
# 3. Traverse the right subtree i.e. call Inorder(right-subtree)
#ouput : 4 2 6 5 7 1 3

def traversal_in(tre):
    trR = tre.get_root()
    inorderlist = []
    
    def inorderTraversal(Node):
        if Node is None:
            return
        inorderTraversal(Node.left)
        inorderlist.append(Node.value)
        inorderTraversal(Node.right)

    inorderTraversal(trR)
    return inorderlist



# Preorder Traversal
# 1. Visit the Node
# 2. Traverse the left subtree i.e. call Preorder(left-subtree)
# 3. Traverse the right subtree i.e. call Preorder(right-subtree)
#ot : 1 2 4 5 6 7 3

def traversal_pre(tre):
    trR = tre.get_root()
    preOrderlist = []
    
    def preOrderTraversal(Node):
        if Node is None:
            return
        preOrderlist.append(Node.value)
        preOrderTraversal(Node.left)
        preOrderTraversal(Node.right)

    preOrderTraversal(trR)
    return preOrderlist


# Postorder Traversal
# 1. Traverse the left subtree i.e. call Postorder(left-subtree)
# 2. Traverse the right subtree i.e. call Postorder(right-subtree)
# 3. Visit the Node
# ot : 4 6 7 5 2 3 1


def traversal_pos(tre):
    trR = tre.get_root()
    posOrderlist = []
    
    def posOrderTraversal(Node):
        if Node is None:
            return
        posOrderTraversal(Node.left)
        posOrderTraversal(Node.right)
        posOrderlist.append(Node.value)

    posOrderTraversal(trR)
    return posOrderlist

tree = Tree()

ls = [1,2,3,4,5,6,7]
for i in ls:
    tree.insert(i)
tree.printTree()    

print('post order ' ,traversal_pos(tree))
print('pre order', traversal_pre(tree))
print('in order ' , traversal_in(tree))