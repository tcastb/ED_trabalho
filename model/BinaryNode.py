# Criação da classe BinaryNode (Nó) que usaremos para ser a classe principal da BinaryTree
class BinaryNode:
    def __init__ (self, data):
        self.data = data
        self.instances = [data]
        self.left = None
        self.right = None