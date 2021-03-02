from queue import PriorityQueue
from nodo import *
from heuristica import *

class Busca:
    
    """[Classe de busca com 3 buscas, A-Estrela, Busca por custo uniforme e A-Estrela simples]
        A-Estrela será representada por A*
        A-Estrela simples será representada por A*s
        Custo uniforme será representado por C
        
        O parametro algoritmo determina o algoritmo a ser usado. Por padrão é usado o A*
    """
    
    # def __init__(self,estado,algoritmo="A*"):
        
    #     #Algoritmo a ser usado
    #     self.algoritmo = algoritmo
    #     self.estado = estado
    
    # def gerarHeuristica(estado,objetivo):
                
    #     heuristica = 0
    #     for i in range(len(estado)):
    #         if(estado[i] != objetivo[i]):
    #             heuristica+=1        
    #     return heuristica
    
    # def gerarCusto(custo):
    #     custo+=1        
    #     return custo
        
    def astar(self,estado, objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]):
        
         #Caminho desejado
        caminho = [] 
        
        # estado =  [1, 2, 3, 4, 5, 6, 7, 0, 8]       
                        
        #Nodos visitados. Escolhi um set para guardar os nodos visitados pois evita repetição de elementos
        visitados = set()
        #Nodos da fronteira. Escolhi lista ordenada pois deixa os elementos na ordem certa para serem visitados
        fronteira = PriorityQueue()
        
        #Criando o nodo inicial que também serve como ponteiro pro nodo atual
        nodo = Nodo(estado, objetivo)
        # print(nodo.estado, "estado")
        # print(nodo.estados, "estados")
               
        #Colocando o nodo atual na fronteira  
        fronteira.put((nodo.f,nodo)) 
        
        if (nodo.estado == nodo.objetivo):
            caminho.append(nodo)
            return caminho       
         
        else:          
            #Removendo da fronteira e adicionando aos visitados               
            visitados.add(fronteira.get()) 
            #Gerando os nodos filhos
            nodo.estados = nodo.gerarEstadosFilhos(estado) 
            # print(nodo.estado, "estado")
            # print(nodo.estados, "estados")
            custo = nodo.custo
            
            for i in range(len(nodo.estados)):
                # print(i)
                aux = nodo.estados[i]
                heuristica = Heuristica(aux, objetivo)
                filho = Nodo(aux,objetivo, heuristica.gerarHeuristica(aux, objetivo), heuristica.gerarCusto(custo), nodo)
                # print(filho.estado, "estado")
                # print(filho.estados, "estados")
                nodo.filhos.append(filho)        
                fronteira.put((filho.f, filho))
                                
            while(nodo.estado != nodo.objetivo):
                
                #Atualizando o nodo atual
                nodo = fronteira.get()[1]             
                #Gerando os filhos do nodo atual
                nodo.estados = nodo.gerarEstadosFilhos(nodo.estado)                                
                #Adicionando o nodo aos visitados
                visitados.add(nodo)
                
                for i in nodo.estados:
                    aux = nodo.estados[i]
                    heuristica = Heuristica(aux, objetivo)
                    filho = Nodo(aux,objetivo, heuristica.gerarHeuristica(aux, objetivo), heuristica.gerarCusto(aux.custo), nodo)
                    nodo.filhos.append(filho)            
                    fronteira.put((filho.f, nodo.filhos[i]))
            
            while(nodo.pai != None):
                caminho.append(nodo.estado)
                nodo = nodo.pai
                               
            return caminho
    
    # def iniciar(self,estado,algoritmo="A*"):
        
    #     if(algoritmo =="A*"):
    #         caminho = self.astar(estado)
    #         print(caminho)   
  
# busca = Busca([1, 2, 3, 4, 5, 6, 7, 0, 8])    
# busca.astar([1, 2, 3, 4, 5, 6, 7, 8, 0])     
busca = Busca()
busca.astar([0, 2, 3, 4, 5, 6, 7, 1, 8])