from mover import *

class Nodo():
    """[Classe de Nodos que irá criar os nodos do grafo]
       [Temos aqui a heuristica h o custo total c  a soma de tudo s e também a referencia para seus nodos filhos]
       
       Como parametros padrão temos:
       [heuristica]: Coloquei como heuristica padrão 8, que seria a heuristica do nodo pai
       [custo]: Coloquei como custo padrão 0, que seria o custo de percorrer o caminho. Como inicia no pai, o custo é 0
       [pai]: Coloquei como pai padrão None, ou seja, o nodo inicial não tem nodo pai
    """
    
    def __init__(self,estado, heuristica=8, custo=0, pai=None):
        
        self.objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        
        #Estado do nodo
        self.estado = estado
        
        #Pai do nodo
        self.pai = pai
        
        self.heuristica = heuristica
        self.custo = custo
        #Estados são os filhos do nodo
        self.estados = []
        self.filhos = []
        #F-value é o custo total, custo+heuristica
        self.f= custo + heuristica
    
    def gerarFilhos(self):
        filho = []
        filho = Mover.moverBranco(filho)
        self.estados.append(filho)
        """
        Loop para gerar nodos filhos. 
        Cria-se nodos filhos passando como parametros:
        [estado]: passa como novo estado o estado calculado anteriormente
        [heuristica]: passa uma função que tem como entrada de parametro o mesmo estado passado como novo estado
        [custo]: passa o custo do pai + 1
        [pai]: como nodo pai, passa o proprio nodo que criou os filhos
        """
        for i in range(len(self.estados)):
            nodoFilho = Nodo(self.estados[i], self.gerarHeuristica(self.estados[i]), self.gerarCusto(self.custo),self)
            self.filhos.append(nodoFilho)
    
    def gerarHeuristica(self):
        
        heuristica = 0
        for i in range(len(self.estado)):
            if(self.estado[i] != self.objetivo[i]):
                heuristica+=1        
        return heuristica
    
    def gerarCusto(custo):
        custo+=1        
        return custo
        
    