# Criação da classe Node (Nó) que usaremos para ser a classe principal da ListaEncadeada
class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None