from model.BinaryNode import BinaryNode

class BinaryTree:
    def __init__(self):
        self.root = None
        self.node_count = 0

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            self.node_count += 1
            return BinaryNode(data)
        
        if data.data.Name == node.data.data.Name:
            node.instances.append(data)
        elif data.data.Name < node.data.data.Name:
            node.left = self._insert(node.left, data)
        elif data.data.Name > node.data.data.Name:
            node.right = self._insert(node.right, data)

        return node

    def search(self, condition):
        return self._search(self.root, condition)

    def _search(self, node, condition):
        if node is None:
            return None

        print(f"Checking node: {node.data.data.Name}")

        comparison_result = condition(node.data.data)

        # if comparison_result == 0:
        #     print(f"Condition met for node: {node.data.data.Name}")
        #     return node.instances
        if comparison_result < 0:
            print("Going left")
            return self._search(node.left, condition)
        else:
            print("Going right")
            return self._search(node.right, condition)

    def display_tree(self):
        return self._display_tree(self.root, "")

    def _display_tree(self, node, prefix):
        result = ""

        if node:
            result += f"{prefix}{node.data.data.Name}\n"
            if node.left or node.right:
                result += f"{prefix}├── Left: {self._display_tree(node.left, prefix + '│   ')}" if node.left else ""
                result += f"{prefix}└── Right: {self._display_tree(node.right, prefix + '    ')}" if node.right else ""

        return result

    def total(self):
        print(f'O total de nós inseridos na àrvore de busca é de: {self.node_count}')
        
    def display(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result