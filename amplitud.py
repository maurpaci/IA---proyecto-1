from Nodo import *
import queue

cola = []

def busquedaPorAmplitud(punto_inicio, punto_meta, ambiente):
    cola = queue.Queue()
    pila = []
    nodoActual = Nodo(None, punto_inicio, ambiente[punto_inicio[0] - 1][punto_inicio[1] - 1], ambiente)
    cola.put(nodoActual)
 
  
    while True:
        
        while (not cola.empty()):
            n = cola.get()
            if (n.estado_actual[0] == punto_meta[0]) and (n.estado_actual[1] == punto_meta[1]):
                return  ListaCamino(n)
            else:
                for i in n.hijos():
                        if (i != None) and (i.ambiente[i.estado_actual[0] - 1][i.estado_actual[1] - 1] != 0):
                            pila.append(i)     
                            
                
        
        while(not (len(pila) == 0)):
            n = pila.pop()
            if (n.estado_actual[0] == punto_meta[0]) and (n.estado_actual[1] == punto_meta[1]):
                return  ListaCamino(n)
            else:
                for i in n.hijos():
                        if (i != None) and (i.ambiente[i.estado_actual[0] - 1][i.estado_actual[1] - 1] != 0):        
                            cola.put(i) 
       
camino_lista = []
def ListaCamino(nodo):
    if nodo.nodo_padre != None:
        camino_lista.append(nodo)
        return ListaCamino(nodo.nodo_padre)
    else:
        camino_lista.append(nodo)
        return camino_lista


            
            