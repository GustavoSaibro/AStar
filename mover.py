class Mover:
    def __init__(self,estado):
        self.estado = estado  
             
    def moverBranco(self,estado):
        estado = self.estado
        if(estado.index(0) == 0):
            estados = []
            estado1 = estado
            estado2 = estado
            aux = estado[0]
            estado1[0] = estado1[1]
            estado1[1] = aux
            estado2[0] = estado2[3]
            estado2[3] = aux
            estados.append(estado1)
            estados.append(estado2)
            return estados

        elif(estado.index(0) == 2):
            estados = []
            estado1 = estado
            estado2 = estado
            aux = estado[2]
            estado1[2] = estado1[3]
            estado1[3] = aux
            estado2[2] = estado2[5]
            estado2[5] = aux
            estados.append(estado1)
            estados.append(estado2)
            return estados

        elif(estado.index(0) == 4):
            estados = []
            estado1 = estado
            estado2 = estado
            estado3 = estado
            estado4 = estado
            aux = estado[4]
            estado1[4] = estado1[1]
            estado1[1] = aux
            estado2[4] = estado2[3]
            estado2[3] = aux
            estado3[4] = estado3[5]
            estado3[5] = aux
            estado4[4] = estado4[7]
            estado4[7] = aux
            estados.append(estado1)
            estados.append(estado2)
            estados.append(estado3)
            estados.append(estado4)
            return estados

        elif(estado.index(0) == 6):
            estados = []
            estado1 = estado
            estado2 = estado
            aux = estado[6]
            estado1[6] = estado1[3]
            estado1[3] = aux
            estado2[6] = estado2[7]
            estado2[7] = aux
            estados.append(estado1)
            estados.append(estado2)
            return estados

        elif(estado.index(0) == 8):
            estados = []
            estado1 = estado
            estado2 = estado
            aux = estado[8]
            estado1[8] = estado1[7]
            estado1[7] = aux
            estado2[8] = estado2[5]
            estado2[5] = aux
            estados.append(estado1)
            estados.append(estado2)
            return estados

        elif(estado.index(0) == 1):
            estados = []
            estado1 = estado
            estado2 = estado
            estado3 = estado
            aux = estado[1]
            estado1[1] = estado1[0]
            estado1[0] = aux
            estado2[1] = estado2[2]
            estado2[2] = aux
            estado3[1] = estado3[4]
            estado3[4] = aux
            estados.append(estado1)
            estados.append(estado2)
            estados.append(estado3)
            return estados

        elif(estado.index(0) == 3):
            estados = []
            estado1 = estado
            estado2 = estado
            estado3 = estado
            aux = estado[3]
            estado1[3] = estado1[0]
            estado1[0] = aux
            estado2[3] = estado2[4]
            estado2[4] = aux
            estado3[3] = estado3[6]
            estado3[6] = aux
            estados.append(estado1)
            estados.append(estado2)
            estados.append(estado3)
            return estados

        elif(estado.index(0) == 5):
            estados = []
            estado1 = estado
            estado2 = estado
            estado3 = estado
            aux = estado[5]
            estado1[5] = estado1[2]
            estado1[2] = aux
            estado2[5] = estado2[4]
            estado2[4] = aux
            estado3[5] = estado3[8]
            estado3[8] = aux
            estados.append(estado1)
            estados.append(estado2)
            estados.append(estado3)
            return estados

        elif(estado.index(0) == 7):
            estados = []
            estado1 = estado
            estado2 = estado
            estado3 = estado
            aux = estado[7]
            estado1[7] = estado1[4]
            estado1[4] = aux
            estado2[7] = estado2[6]
            estado2[6] = aux
            estado3[7] = estado3[8]
            estado3[8] = aux
            estados.append(estado1)
            estados.append(estado2)
            estados.append(estado3)
            return estados

        
