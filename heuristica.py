class Heuristica:
    
    def __init__(self, estado, objetivo):
        self.estado = estado
        self.objetivo = objetivo
        
    
    def gerarHeuristica(self,estado,objetivo):
                
        heuristica = 0
        for i in range(len(estado)):
            if(estado[i] != objetivo[i]):
                heuristica+=1        
        return heuristica
    
    def gerarCusto(self,custo):
        custo+=1        
        return custo
    
    