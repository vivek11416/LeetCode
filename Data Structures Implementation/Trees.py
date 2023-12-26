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