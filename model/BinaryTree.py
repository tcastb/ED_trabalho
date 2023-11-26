from model.BinaryNode import BinaryNode

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return BinaryNode(data)

        if data.Name < root.data.Name:
            root.left = self._insert(root.left, data)
        elif data.Name > root.data.Name:
            root.right = self._insert(root.right, data)

        return root

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, root, value):
        if root is None or root.data.Name == value:
            return root

        if value < root.data.Name:
            return self._search(root.left, value)
        else:
            return self._search(root.right, value)

    def inorder_traversal(self, root, result):
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.data)
            self.inorder_traversal(root.right, result)

    def display(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result