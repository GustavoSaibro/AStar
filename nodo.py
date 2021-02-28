from mover import *

class Nodo:
    """[Classe de Nodos que irá criar os nodos do grafo]
       [Temos aqui a heuristica h o custo total c  a soma de tudo s e também a referencia para seus nodos filhos]
       
       Como parametros padrão temos:
       [heuristica]: Coloquei como heuristica padrão 8, que seria a heuristica do nodo pai
       [custo]: Coloquei como custo padrão 0, que seria o custo de percorrer o caminho. Como inicia no pai, o custo é 0
       [pai]: Coloquei como pai padrão None, ou seja, o nodo inicial não tem nodo pai
    """
    
    def __init__(self,estado, objetivo, heuristica=8, custo=0, pai=None):
        
        self.objetivo = objetivo
        
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
        self.f = custo + heuristica
    
    def gerarEstadosFilhos(self,estado):
        filho = []  

        mover = Mover(estado)        
        filho = mover.moverBranco(estado)    
        estados = self.estados.append(filho)
        
        return estados
    

        
    