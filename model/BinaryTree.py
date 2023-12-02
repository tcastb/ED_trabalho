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
        result = []
        self._search(self.root, condition, result)
        return result

    def _search(self, node, condition, result):
        if node is None:
            return None

        if condition(node.data.data):
            result.extend(node.instances)

        self._search(node.left, condition, result)

        self._search(node.right, condition, result)

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

    def node_total(self):
        print(f'O total de nós inseridos na àrvore de busca é de: {self.node_count}')
        
    def register_total(self):
        total_count = self._register_total(self.root)
        print(f'O total de registros inseridos na árvore de busca é de: {total_count}')

    def _register_total(self, node):
        if node:
            # Contar o próprio nó e todos os nós nas listas 'instances'
            count = 1 + len(node.instances)
            # Recursivamente contar os nós à esquerda e à direita
            count += self._register_total(node.left) + self._register_total(node.right)
            return count
        else:
            return 0
        
    def display(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result