class Node:
    """Node in a BST."""

    def __init__(self, value, left=None, right=None):

        self.value = value
        self.left = left
        self.right = right

    def find_recursively(self, value):

        def _traverse(node, value):
            if not node:
                return None
            if value == node.value:
                return value
            
            if value < node.value:
                return _traverse(node.left, value)
            else:
                return _traverse(node.right, value)
            
        return _traverse(self, value)
    
    def df_preorder_traversal(self):

        seen = []

        def _traverse(node, seen):
            if not node:
                return seen
            
            seen.append(node.value)

            if node.left:
                seen + _traverse(node.left, seen)
            if node.right:
                seen + _traverse(node.right, seen)

            return seen

        return _traverse(self, seen)
    
    def df_inorder_traversal(self):

        seen = []
        def _traverse(node, seen):
            if not node:
                return seen

            if node.left:
                seen + _traverse(node.left, seen)

            seen.append(node.value)

            if node.right:
                seen + _traverse(node.right, seen)

            return seen

        return _traverse(self, seen)
    
    def df_postorder_traversal(self):

        seen = []
        def _traverse(node, seen):
            if not node:
                return seen

            if node.left:
                seen + _traverse(node.left, seen)
            if node.right:
                seen + _traverse(node.right, seen)

            seen.append(node.value)

            return seen

        return _traverse(self, seen)


class BST:
    """Binary Search Tree"""

    def __init__(self, root):
        self.root = root

    def insert(self, value):
        current = self.root
        prev = None

        while current:
            if value < current.value:
                prev = current
                current = current.left

            else:
                prev = current
                current = current.right

        if value < prev.value:
            prev.left = Node(value)
        else:
            prev.right = Node(value)

    def find(self, value):

        current = self.root
        while current and current.value != value:
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current and current.value == value:
            return current
        else:
            return None
        
    def find_recursively(self, value):
        return self.root.find_recursively(value)
    
    def df_preorder_traversal(self):
        return self.root.df_preorder_traversal()
    
    def df_inorder_traversal(self):
        return self.root.df_inorder_traversal()
    
    def df_postorder_traversal(self):
        return self.root.df_postorder_traversal()

if __name__ == "__main__":
    binarySearchTree = BST(Node(15))
    binarySearchTree.insert(20)
    binarySearchTree.insert(10)
    binarySearchTree.insert(12)
    if binarySearchTree.root.value != 15:
        print("Error! Root value should be 15")
    if binarySearchTree.root.right.value != 20:
        print("Error! Right value should be 20")
    if binarySearchTree.root.left.right.value != 12:
        print("Error! Left value should be 12")

    if binarySearchTree.find(20).value != 20:
        print("Error! Should have found node with value 20")

    if binarySearchTree.find(200) != None:
        print("Error! Not find node with value 200")

    if binarySearchTree.find_recursively(20) != 20:
        print("Error! Should have found node with value 20")

    if binarySearchTree.find_recursively(200) != None:
        print("Error! Not find node with value 200")

    bst = BST(Node(15))
    bst.insert(20)
    bst.insert(10)
    bst.insert(12)
    bst.insert(1)
    bst.insert(5)
    bst.insert(50)
    seen = bst.df_preorder_traversal()
    if seen != [15, 10, 1, 5, 12, 20, 50]:
        print(f"Error! Pre-order traversal order should be [15, 10, 1, 5, 12, 20, 50] not {seen}")

    seen = bst.df_inorder_traversal()
    if seen != [1, 5, 10, 12, 15, 20, 50]:
        print(f"Error! In-order traversal order should be [1, 5, 10, 12, 15, 20, 50] not {seen}")

    seen = bst.df_postorder_traversal()
    if seen != [5, 1, 12, 10, 50, 20, 15]:
        print(f"Error! Post-order traversal order should be [5, 1, 12, 10, 50, 20, 15] not {seen}")
    

        