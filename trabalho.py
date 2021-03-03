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

    def astar(self, estado, objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]):

        #Caminho desejado
        caminho = [] 
        
        qtNodosVis = 0
        qtNodosCri = 0
        tamFront = 0
        tamCamin = 0
                        
        #Nodos visitados. Escolhi um set para guardar os nodos visitados pois evita repetição de elementos
        visitados = set()
        #Nodos da fronteira. Escolhi lista ordenada pois deixa os elementos na ordem certa para serem visitados
        fronteira = PriorityQueue()
        
        #Criando o nodo inicial que também serve como ponteiro pro nodo atual
        nodo = Nodo(estado, objetivo)
        
        #Lista para guardar os ponteiros dos nodos filhos
        nodos = []
  
        #Colocando o nodo atual na fronteira  
        fronteira.put((nodo.custoF(), nodo)) 

        print(fronteira.get())
        
        if (nodo.estado == nodo.objetivo):
            caminho.append(nodo)
            print("quantidade de nodos visitados: ", qtNodosVis)
            print("quantidade de nodos criados: ", qtNodosCri)
            print("tamanho da fronteira: ", tamFront)
            print("tamanho do caminho: ", tamCamin)
            return caminho       
         
        else:          
            #Removendo da fronteira e adicionando aos visitados               
            visitados.add(fronteira.get()) 
            #Gerando os nodos filhos
            nodo.estados = nodo.gerarEstadosFilhos(estado) 

            custo = nodo.custo
            
            
            for i in range(len(nodo.estados)):
                aux = nodo.estados[i]
                heuristica = Heuristica(aux, objetivo)
                filho = Nodo(aux,objetivo, heuristica.gerarHeuristica(aux, objetivo), heuristica.gerarCusto(custo), nodo)
                nodos.append(filho)

                nodo.filhos.append(filho)        
                fronteira.put((filho.custoF(), filho))
                
                #Aumentando os parametros
                qtNodosVis +=1
                qtNodosCri +=1
                tamFront +=1
                tamCamin +=1
                                
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
                    fronteira.put((filho.custoF(), nodo.filhos[i]))
                    
                    #Aumentando os parametros
                    qtNodosVis +=1
                    qtNodosCri +=1
                    tamFront +=1
                    tamCamin +=1
            
            while(nodo.pai != None):
                caminho.append(nodo.estado)
                nodo = nodo.pai
            
            print("quantidade de nodos visitados: ", qtNodosVis)
            print("quantidade de nodos criados: ", qtNodosCri)
            print("tamanho da fronteira: ", tamFront)
            print("tamanho do caminho: ", tamCamin)                   
            return caminho
    
    def astarSimple(self, estado, objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]):
        
        #Caminho desejado
        caminho = [] 
        
        qtNodosVis = 0
        qtNodosCri = 0
        tamFront = 0
        tamCamin = 0
        
        #Nodos visitados. Escolhi um set para guardar os nodos visitados pois evita repetição de elementos
        visitados = set()
        #Nodos da fronteira. Escolhi lista ordenada pois deixa os elementos na ordem certa para serem visitados
        fronteira = PriorityQueue()
        
        #Criando o nodo inicial que também serve como ponteiro pro nodo atual
        nodo = Nodo(estado, objetivo)
        
        #Lista para guardar os ponteiros dos nodos filhos
        nodos = []
               
        #Colocando o nodo atual na fronteira  
        fronteira.put((nodo.f,nodo)) 
        
        if (nodo.estado == nodo.objetivo):
            caminho.append(nodo)
            print("quantidade de nodos visitados: ", qtNodosVis)
            print("quantidade de nodos criados: ", qtNodosCri)
            print("tamanho da fronteira: ", tamFront)
            print("tamanho do caminho: ", tamCamin)
            return caminho       
         
        else:          
            #Removendo da fronteira e adicionando aos visitados               
            visitados.add(fronteira.get()) 
            #Gerando os nodos filhos
            nodo.estados = nodo.gerarEstadosFilhos(estado) 

            custo = nodo.custo

            for i in range(len(nodo.estados)): 
                aux = nodo.estados[i]
                heuristica = Heuristica(aux, objetivo)
                filho = Nodo(aux,objetivo, heuristica.gerarHeuristica(aux, objetivo), heuristica.gerarCusto(custo), nodo)
                nodos.append(filho)
                nodo.filhos.append(filho)        
                fronteira.put((filho.heuristica(), filho))
                
                #Aumentando os parametros
                qtNodosVis +=1
                qtNodosCri +=1
                tamFront +=1
                tamCamin +=1
                                
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
                    fronteira.put((filho.heuristica(), nodo.filhos[i]))
                    
                    #Aumentando os parametros
                    qtNodosVis +=1
                    qtNodosCri +=1
                    tamFront +=1
                    tamCamin +=1
                                
            while(nodo.pai != None):
                caminho.append(nodo.estado)
                nodo = nodo.pai
            
            print("quantidade de nodos visitados: ", qtNodosVis)
            print("quantidade de nodos criados: ", qtNodosCri)
            print("tamanho da fronteira: ", tamFront)
            print("tamanho do caminho: ", tamCamin)                   
            return caminho
        
    
    def custoUniforme(self, estado, objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]):
        
         #Caminho desejado
        caminho = [] 
        
        qtNodosVis = 0
        qtNodosCri = 0
        tamFront = 0
        tamCamin = 0
        
        #Nodos visitados. Escolhi um set para guardar os nodos visitados pois evita repetição de elementos
        visitados = set()
        #Nodos da fronteira. Escolhi lista ordenada pois deixa os elementos na ordem certa para serem visitados
        fronteira = PriorityQueue()
        
        #Criando o nodo inicial que também serve como ponteiro pro nodo atual
        nodo = Nodo(estado, objetivo)

        #Lista para guardar os ponteiros dos nodos filhos
        nodos = []
        
        #Colocando o nodo atual na fronteira  
        fronteira.put((nodo.f,nodo)) 
        
        if (nodo.estado == nodo.objetivo):
            caminho.append(nodo)
            print("quantidade de nodos visitados: ", qtNodosVis)
            print("quantidade de nodos criados: ", qtNodosCri)
            print("tamanho da fronteira: ", tamFront)
            print("tamanho do caminho: ", tamCamin)   
            return caminho       
         
        else:          
            #Removendo da fronteira e adicionando aos visitados               
            visitados.add(fronteira.get()) 
            #Gerando os nodos filhos
            nodo.estados = nodo.gerarEstadosFilhos(estado) 

            custo = nodo.custo
            
            for i in range(len(nodo.estados)):
       
                aux = nodo.estados[i]
                heuristica = Heuristica(aux, objetivo)
                filho = Nodo(aux,objetivo, heuristica.gerarHeuristica(aux, objetivo), heuristica.gerarCusto(custo), nodo)
                nodos.append(filho)
                
                nodo.filhos.append(filho)        
                fronteira.put((filho.custoC(), filho))
                
                #Aumentando os parametros
                qtNodosVis +=1
                qtNodosCri +=1
                tamFront +=1
                tamCamin +=1
                                
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
                    fronteira.put((filho.custoC(), nodo.filhos[i]))
                    
                    
                    #Aumentando os parametros
                    qtNodosVis +=1
                    qtNodosCri +=1
                    tamFront +=1
                    tamCamin +=1
            
            while(nodo.pai != None):
                caminho.append(nodo.estado)
                nodo = nodo.pai
            
            print("quantidade de nodos visitados: ", qtNodosVis)
            print("quantidade de nodos criados: ", qtNodosCri)
            print("tamanho da fronteira: ", tamFront)
            print("tamanho do caminho: ", tamCamin)                     
            return caminho
  
 
busca = Busca()
busca.astar([0, 2, 3, 4, 5, 6, 7, 1, 8])