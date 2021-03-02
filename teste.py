from queue import PriorityQueue

class Pessoa():
    
    def __init__(self,prioridade ,nome):
        self.prioridade = prioridade
        self.nome = nome
        
    

lista = PriorityQueue()
pessoa = Pessoa(5,[1,2])
pessoa2 = Pessoa(6,[2,3])
lista.put((pessoa.prioridade, pessoa))
lista.put((pessoa2.prioridade, pessoa2))

print(lista.get())
print(lista.get())
        