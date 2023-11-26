# Gerando a classe do dataframe que utilizaremos no projeto
class Science:
    def __init__(self, name, company, location, description, salary):
        self.name = name
        self.company = company
        self.location = location
        self.description = description
        self.salary = salary
        
    def __str__(self):
        return f"Name: {self.name}, Company: {self.company}, Location: {self.location}, Salary: {self.salary}"
    
    @staticmethod
    def showById(lst, idx):
        if 0 <= idx < len(lst):
            print(f'Recuperado da lista o objeto de id: {idx}')
            item = lst[idx]
            print(f"Name: {item.name}," +
                  f"\nCompany: {item.company}," +
                  f"\nLocation: {item.location}," +
                  f"\nDescription: {item.description}," +
                  f"\nSalary: {item.salary}")
        else:
            print(f"O index informado ({idx}) não existe, por favor, selecione algo entre 0 e {len(lst)-1}.")

    @staticmethod
    def showAll(lst, top = None):
        if top is not None:
            print(f'Mostrando o(s) {top} primeiro(s) registro(s).')
            lst = lst[:top]
            
        for idx, item in enumerate(lst):
            print(f"ID: {idx}, Name: {item.name}, Company: {item.company}, Location: {item.location}, Description: {item.description}, Salary: {item.salary}")