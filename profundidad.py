from Nodo import *
    
def BusquedaProfundidadIterativa(punto_inicio, punto_meta, ambiente):
    limite = 0
    while True:
        raiz =  Nodo(None, punto_inicio, 0 , ambiente)
        pila = [(raiz , 0)]
        while len(pila) != 0:
            elemento = pila.pop()
            nodo = elemento[0]
            profundidad_actual = elemento[1]
            
           
            if(nodo.estado_actual == punto_meta):
                return ListaCamino(nodo)
            if profundidad_actual < limite:
                for i in nodo.hijos():
                    if (i != None) and (i.ambiente[i.estado_actual[0] - 1][i.estado_actual[1] - 1] != 0):
                        pila.append((i, profundidad_actual + 1))
        limite = limite + 1
         
camino_lista = []
def ListaCamino(nodo):
    if nodo.nodo_padre != None:
        camino_lista.append(nodo)
        return ListaCamino(nodo.nodo_padre)
    else:
        camino_lista.append(nodo)
        return camino_lista


