class Node:
    def __init__(self,data):
        self.data = data
        self.right_child = None
        self.left_child = None

n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4

#all left node traversal
# current = n1
# while current:
#     print(current.data)
#     current = current.left_child

# types of traversal = in-order , pre-order , post-order
#https://www.youtube.com/watch?v=4_UDUj1j1KQ
def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)


#inorder(n1)

def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)

#preorder(n1)
# all left then right
def postorder(root_node):
    current = root_node
    if current is None:
        return

    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data)

#postorder(n1)

#levelorder
from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.right_child = None
        self.left_child = None

n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4


def levelOrder(root_node):
    list_of_nodes = []
    traversal_queue = deque([root_node])
    while len(traversal_queue)>0:
        node = traversal_queue.popleft()
        list_of_nodes.append(node.data)
        if node.left_child:
            traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)

    return list_of_nodes

#print(levelOrder(n1))

#Expression tree #postfix notation
class TreeNode:
    def __init__(self,data=None):
        self.data = data
        self.right = None
        self.left = None

class Stack:
    def __init__(self):
        self.elements = []

    def push(self,item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()


expr = "4 5 + 5 3 - *".split()
stack = Stack()


for term in expr:
    if term in "+-*/":
        node = TreeNode(data=term)
        node.right = stack.pop()
        node.left = stack.pop()

    else:
        node = TreeNode(data=int(term))
    stack.push(node)

def calc(node):
    if node.data == "+":
        return calc(node.left) + calc(node.right)
    elif node.data == "-":
        return calc(node.left) - calc(node.right)
    elif node.data == "*":
        return calc(node.left) * calc(node.right)
    elif node.data == "/":
        return calc(node.left) / calc(node.right)
    else:
        return node.data

# root = stack.pop()
# result = calc(root)
# print(result)
#(4+5)*(5-3) = 18

#binary Search trees
# the left node value is less than equal to node and right node value is greater than root node .
# Let K1 = root node , K2 = left child , K3 = right child then K2 <= K1 and K3 > K1

class Node:
    def __init__(self,data):
        self.data = data
        self.right_child = None
        self.left_child = None
class Tree:
    def __init__(self):
        self.root_node = None

    def insert(self,data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return self.root_node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data <= parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return self.root_node
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return self.root_node

    def search(self,data):
        current = self.root_node
        while True:
            if current is None:
                print("Item not found")
                return None
            elif current.data is data:
                print("Item Found")
                return data
            else:
                if data <= current.data:
                    current = current.left_child
                else:
                    current = current.right_child


    def inorder(self,root_node):
        current = root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)

# tree = Tree()
# r=tree.insert(5)
# r=tree.insert(2)
# r=tree.insert(7)
# r=tree.insert(9)
# r=tree.insert(1)
#
# print(tree.search(6))

# Deleting Node 210
# if node to be deleted has children we replace the node with the successor node -  successor node is the node that has minimum value in the right subtree of the node to be deleted

    def get_node_with_parent(self,data):
        parent = None
        current = self.root_node
        if current is None:
            return (parent,None)

        while True:
            if current.data == data:
                return (parent,current)
            elif current.data > data:
                parent = current
                current = current.left_child

            else:
                parent = current
                current = current.right_child

        return (parent,current)

    def remove(self,data):
        parent,node = self.get_node_with_parent(data)

        if parent is None and node is None:
            return False

        children_count = 0

        if node.left_child and node.right_child:
            children_count = 2

        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0

        else:
            children_count = 1

        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None

                else:
                    parent.left_child = None

            else:
                self.root_node = None

        elif children_count == 1:
            next_node = None

            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child


            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node

                else:
                    parent.right_child = next_node

            else:
                self.root_node = next_node

        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child

            node.data = leftmost_node.data

            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child

            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child


    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child

        return current.data

    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child

        return current.data


tree = Tree()
r=tree.insert(5)
r=tree.insert(2)
r=tree.insert(7)
r=tree.insert(9)
r=tree.insert(1)

print(tree.search(9))
tree.remove(9)
print(tree.search(9))



