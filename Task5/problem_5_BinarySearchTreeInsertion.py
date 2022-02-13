class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)

    # The function to be written in hackerRank.
    def insert(self, val):
        # Enter you code here.
        current = self.root  # A pointer to the root
        # checking if the tree is empty.
        if current is None:
            self.root = Node(val)
            return self.root
        # If the value is bigger go right.
        while current is not None:
            if val > current.info:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    break
            # If the value is lower go left.
            else:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    break
        return self.root


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
