from Nodo import *
import queue


def busquedaPorCosto(punto_inicio, punto_meta, ambiente):
    lista = queue.PriorityQueue()
    
    nodoActual = Nodo(None, punto_inicio, 0,ambiente)
    
    lista.put(nodoActual)
    
    while True:
        
        n = lista.get()
        if(n.estado_actual == punto_meta):
            return ListaCamino(n)
        else:
            for i in n.hijos():
                if (i!=None) and (i.ambiente[i.estado_actual[0] - 1][i.estado_actual[1] - 1] != 0):
                    lista.put(i)
    
camino_lista = []
def ListaCamino(nodo):
    if nodo.nodo_padre != None:
        camino_lista.append(nodo)
        return ListaCamino(nodo.nodo_padre)
    else:
        camino_lista.append(nodo)
        return camino_lista
    