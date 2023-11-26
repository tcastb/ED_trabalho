from model.Node import Node

# Criação da classe ListaEncadeada que será a nossa classe que cuidará da Lista em si
class ListaEncadeada:
    def __init__ (self):
        # Definimos aqui o primeiro objeto da lista como None, assim que a lista
        # for instanciada, a mesma já iniciará com um objeto vazio
        self.first = None
    
    # Metódo "insert"
    # Este método será utilizado para cuidar do encadeamento dos objetos em ordem
    def insert (self, new_data):
        # É verifica se a lista está vazia, estando vazia, ele adiciona o primeiro objeto
        if self.first is None:
            self.first = new_data
        else:
            # Caso na condição anterior, a lista já possuir um objeto, ele irá usar
            # o primeiro objeto para adicionar o próximo objeto no encadeamento
            # do objeto, deixando ele como o próximo na lista
            data = self.first
            while data.next is not None:
                data = data.next
            data.next = new_data

    # Método "show"
    # Este método será utilizado para cuidar da amostragem da lista
    def show (self):
        data = self.first
        while data is not None:
            print(data.data)
            data = data.next

    # Método "filter"
    # Este método será utilizado para filtrar a lista instanciada utilizando o sistema
    # de lambda no próprio parâmetro, facilitando assim a consulta à lista
    def filter (self, condition):
        current = self.first
        list = ListaEncadeada()

        while current is not None:
            if condition(current.data):
                list.insert(Node(current.data))
            current = current.next

        return list

    # Método "sort"
    # Este método será utilizado para orderna a lista instanciada utilizando o sistema
    # de lambda no próprio parâmetro, facilitando a escolha da ordenação
    def sort (self, key=None, reverse=False):
        list = self.to_list()
        list.sort(key = key, reverse = reverse)

        sorted_list = ListaEncadeada()
        for i in list:
            sorted_list.insert(Node(i))

        return sorted_list

    # Método "to_list"
    # Este método será utilizado para tranformar a lista encadeada em uma lista comum
    # desta forma será possível utilizar comandos de ordenação e filtragem diretamente
    # na lista instanciada.
    def to_list (self):
        list = []
        current = self.first

        while current is not None:
            list.append(current.data)
            current = current.next

        return list