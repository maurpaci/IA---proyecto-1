class Nodo:
    
    def __init__(self, nodo_padre, estado_actual, costo , ambiente):
        self.nodo_padre = nodo_padre
        self.estado_actual = estado_actual
        if(self.nodo_padre == None):
            self.costo = 0
        else: 
            self.costo = costo + self.nodo_padre.costo
        self.ambiente = ambiente
        self.camino = ""
        
    def hijos (self) :
        hijos = []
        
        
        if  self.estado_actual[1] > 1:
            arriba = Nodo(self, (self.estado_actual[0] , self.estado_actual[1] - 1), self.ambiente[self.estado_actual[0] - 1][self.estado_actual[1] - 1], self.ambiente)
            hijos.append(arriba)
        else:
            hijos.append(None)
        
        
        if (self.estado_actual[0] < 5):
            derecha = Nodo(self, (self.estado_actual[0] + 1 , self.estado_actual[1]), self.ambiente[self.estado_actual[0] - 1][self.estado_actual[1] - 1], self.ambiente)
            hijos.append(derecha)
        else:
            hijos.append(None)
        
        
        if (self.estado_actual[1] < 5):
            abajo = Nodo(self, (self.estado_actual[0] , self.estado_actual[1] + 1), self.ambiente[self.estado_actual[0]-1][self.estado_actual[1]-1], self.ambiente)
            hijos.append(abajo)
        else:
            hijos.append(None)
        
        
        
        if (self.estado_actual[0] > 1):
            izquierda = Nodo(self, (self.estado_actual[0] - 1 , self.estado_actual[1]), self.ambiente[self.estado_actual[0]-1][self.estado_actual[1]-1], self.ambiente)
            hijos.append(izquierda)
        else:
            hijos.append(None)
        
        
        return hijos
    
    def __lt__(self, otro):
        return (self.costo) < (otro.costo)
        
    def __str__(self):
        return "(" + str(self.estado_actual[0]) + "," + str(self.estado_actual[1]) + ")"
    
    
       
       




