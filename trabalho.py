from queue import PriorityQueue
from nodo import *

class Busca(object):
    
    """[Classe de busca com 3 buscas, A-Estrela, Busca por custo uniforme e A-Estrela simples]
        A-Estrela será representada por A*
        A-Estrela simples será representada por A*s
        Custo uniforme será representado por C
        
        O parametro algoritmo determina o algoritmo a ser usado. Por padrão é usado o A*
    """
    
    def __init__(self,algoritmo="A*"):
        
        #Algoritmo a ser usado
        self.algoritmo = algoritmo
        
    def astar(estado, objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]):
        
         #Caminho desejado
        caminho = []   
                
        #Nodos visitados. Escolhi um set para guardar os nodos visitados pois evita repetição de elementos
        visitados = set()
        #Nodos da fronteira. Escolhi lista ordenada pois deixa os elementos na ordem certa para serem visitados
        fronteira = PriorityQueue()
        
        #Criando o nodo inicial que também serve como ponteiro pro nodo atual
        nodo = Nodo(estado, objetivo)

        
        #Colocando o nodo atual na fronteira  
        fronteira.put((nodo.heuristica,nodo))
        
        if (nodo.estado == nodo.objetivo):
            caminho.append(nodo)
            return caminho       
         
        else:
            #Removento da fronteira e adicionando aos visitados               
            visitados.add(fronteira.get()) 
            #Gerando os nodos filhos
            nodo.gerarFilhos() 
                        
            for i in nodo.filhos:
                fronteira.put((nodo.filhos[i].f, nodo.filhos[i]))
                                
            while(nodo.estado != nodo.objetivo):
                
                #Atualizando o nodo atual
                nodo = fronteira.get()[1]                
                #Gerando os filhos do nodo atual
                nodo.gerarFilhos()                
                #Adicionando o nodo aos visitados
                visitados.add(nodo)
                                
                for i in nodo.filhos:
                    fronteira.put((nodo.filhos[i].f, nodo.filhos[i]))
            
            while(nodo.pai != None):
                caminho.add(nodo.estado)
                nodo = nodo.pai
                               
            return caminho
    
    def iniciar(self,algoritmo="A*"):
        
        if(algoritmo =="A*"):
            caminho = self.astar([1, 2, 3, 4, 5, 6, 7, 0, 8])
            print(caminho)   
                
busca = Busca()
busca.iniciar()   