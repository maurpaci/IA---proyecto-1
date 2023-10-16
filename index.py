import tkinter as tk 
from tkinter import messagebox
import amplitud
import costo
import profundidad
from PIL import Image, ImageTk
root = tk.Tk()

root.geometry("1000x1000")
# Creacion de la interfaz grafica del menu de opciones
panel_principal = tk.Frame(root)
panel_principal.config(bg = "LightGoldenrod2", width="1000", height="1000")
panel_principal.grid(row= 0 , column=0)

tk.Label(panel_principal,text="Ingrese el nodo inicio: ").grid(row=0, column=0, padx=5, pady=5)
entrada_nodoInicio = tk.Entry(panel_principal)
entrada_nodoInicio.insert(0, "1,5")
entrada_nodoInicio.grid(row=0,column=1)


tk.Label(panel_principal,text="Ingrese el nodo meta: ").grid(row=1, column=0, padx=5, pady=5)
entrada_nodoMeta = tk.Entry(panel_principal)
entrada_nodoMeta.insert(0, "5,5")
entrada_nodoMeta.grid(row=1,column=1)

panel_matriz = tk.Frame(panel_principal ,bg="white", borderwidth=1, relief='solid')
panel_matriz.grid(row=2, column=0, columnspan=5)

#Creacion de la interfaz grafica del laberinto
def GUIcreation():
    global matriz_paneles 
    matriz_paneles = []
    for i in range(5):
        fila_matriz = []
        for j in range(5):
            panel = tk.Frame(panel_matriz)
            panel.config(width= 180, height=90, borderwidth=1.5, relief='solid', )
            panel.grid(row=i, column=j)
            fila_matriz.append(panel)
        matriz_paneles.append(fila_matriz)

GUIcreation()

# LIMPIAR EL TABLERO PARA EL CASO DE REINICIAR
def eliminar_labels():
    for i in range(len(matriz_paneles)):
        for j in range(len(matriz_paneles)):
            borrar_label_si_existe(matriz_paneles[i][j])
            
def borrar_label_si_existe(panel):
    widgets = panel.winfo_children()  

    for widget in widgets:
        if isinstance(widget, tk.Label):
            widget.destroy() 
            
def eliminar_label_raiz():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()
            
            
# LEER EL AMBIENTE DESDE EL ARCHIVO DE TEXTO ambiente.txt
def obtenerEscenario():
    eliminar_labels()
    eliminar_label_raiz()
    global ambiente
    obtener_ambiente = open("ambiente.txt" , "r")
    ambiente = obtener_ambiente.read()
    ambiente = ambiente.split("\n")
    obtener_ambiente.close()
    
    for i in range(0, len(ambiente)):
        ambiente[i] = ambiente[i].split(" ")
    
    #Convertir la matriz leia de char a enteros
    for i in range(0, len(ambiente)):
        for j in range(0,len(ambiente)):
            ambiente[i][j] = int(ambiente[i][j])
    
    
    for i in range(len(ambiente)):
       
            for j in range(len(ambiente)):
                if ambiente[i][j] == 0:
                    matriz_paneles[i][j].config(bg="black")
                if ambiente[i][j] == 2:
                    matriz_paneles[i][j].config(bg="blue")
                if ambiente[i][j] == 3:
                    matriz_paneles[i][j].config(bg="brown",)
        
#_________________________Busqueda Amplitud_____________
def busqueda_amplitud():
    labelSolucion = ""
    boton_amplitud.config(state="disabled")
    boton_costo.config(state="disabled")
    boton_profundidad.config(state = "disabled")
    boton_nuevo_camino.config(state="normal")
    
    
    obtener_coordenadas_inicio = entrada_nodoInicio.get()
    obtener_coordenadas_inicio = obtener_coordenadas_inicio.split(',')
    
    obtener_coordenadas_meta = entrada_nodoMeta.get()
    obtener_coordenadas_meta = obtener_coordenadas_meta.split(',')
    
    inicio = (int(obtener_coordenadas_inicio[0]) , int( obtener_coordenadas_inicio[1]))
    meta = ( int(obtener_coordenadas_meta[0]) , int(obtener_coordenadas_meta[1]))
    
    if (ambiente[inicio[0] - 1][inicio[1] - 1] == 0 or ambiente[meta[0] - 1][meta[1] - 1] == 0):
        messagebox.showinfo("Error","El punto de inicio o fin no estan disponibles en este ambiente (casilla negra)")
    else:        
        tk.Label(matriz_paneles[inicio[0] - 1][inicio[1] - 1], text="INICIO" ).place(x=25, y = 0)
        tk.Label(matriz_paneles[meta[0] - 1][meta[1] - 1], text="Geppeto - META" ).place(x=25, y = 0)
        
        labelSolucion = "Camino Solución:  \n Meta "
        
        for i in amplitud.busquedaPorAmplitud(inicio,meta,ambiente):
            x = i.estado_actual[0]
            y = i.estado_actual[1]
            
            labelSolucion = labelSolucion + "<- (" + str(i.estado_actual[0]) + ","+ str(i.estado_actual[1]) +  ") "
        
            labelCamino = tk.Label(matriz_paneles[x-1][y-1], text="P",bg="green")
            labelCamino.place(x = 40 , y =20)
        
        labelSolucion = labelSolucion + " <- Inicio"
        label = tk.Label(root, text=labelSolucion) 
        label.grid(row=1, column=0)
        
           
#_________________________Busqueda costo_____________
        
def busqueda_costo():  
    labelSolucion = ""
    boton_amplitud.config(state="disabled")
    boton_costo.config(state="disabled")
    boton_profundidad.config(state = "disabled")
    boton_nuevo_camino.config(state="normal")
      
    obtener_coordenadas_inicio = entrada_nodoInicio.get()
    obtener_coordenadas_inicio = obtener_coordenadas_inicio.split(',')
    
    obtener_coordenadas_meta = entrada_nodoMeta.get()
    obtener_coordenadas_meta = obtener_coordenadas_meta.split(',')
    
    inicio = (int(obtener_coordenadas_inicio[0]) , int( obtener_coordenadas_inicio[1]))
    meta = ( int(obtener_coordenadas_meta[0]) , int(obtener_coordenadas_meta[1]))
    
    if (ambiente[inicio[0] - 1][inicio[1] - 1] == 0 or ambiente[meta[0] - 1][meta[1] - 1] == 0):
        messagebox.showinfo("Error","El punto de inicio o fin no estan disponibles en este ambiente (casilla negra)")
    else:
        tk.Label(matriz_paneles[inicio[0] - 1][inicio[1] - 1], text="INICIO" ).place(x=25, y = 0)
        tk.Label(matriz_paneles[meta[0] - 1][meta[1] - 1], text="Geppeto - META" ).place(x=25, y = 0)
        
        labelSolucion = "Camino Solución:  \n Meta "
        
        for i in costo.busquedaPorCosto(inicio,meta,ambiente):
            x = i.estado_actual[0]
            y = i.estado_actual[1]
            labelSolucion = labelSolucion + "<- (" + str(i.estado_actual[0]) + ","+ str(i.estado_actual[1]) +  ") "
            
            labelCamino = tk.Label(matriz_paneles[x-1][y-1], text="P",bg="green")
            labelCamino.place(x = 40 , y =20)
            
        
        
        labelSolucion = labelSolucion + " <- Inicio"
        label = tk.Label(root, text=labelSolucion) 
        label.grid(row=1, column=0)


#-------------Profundidad----------

def busqueda_profundidad():
    labelSolucion = ""
    boton_amplitud.config(state="disabled")
    boton_costo.config(state="disabled")
    boton_profundidad.config(state = "disabled")
    boton_nuevo_camino.config(state="normal")
    
    obtener_coordenadas_inicio = entrada_nodoInicio.get()
    obtener_coordenadas_inicio = obtener_coordenadas_inicio.split(',')
    
    obtener_coordenadas_meta = entrada_nodoMeta.get()
    obtener_coordenadas_meta = obtener_coordenadas_meta.split(',')
    
    inicio = (int(obtener_coordenadas_inicio[0]) , int( obtener_coordenadas_inicio[1]))
    meta = ( int(obtener_coordenadas_meta[0]) , int(obtener_coordenadas_meta[1]))
    if (ambiente[inicio[0] - 1][inicio[1] - 1] == 0 or ambiente[meta[0] - 1][meta[1] - 1] == 0):
        messagebox.showinfo("Error","El punto de inicio o fin no estan disponibles en este ambiente (casilla negra)")    
    else:
        tk.Label(matriz_paneles[inicio[0] - 1][inicio[1] - 1], text="INICIO" ).place(x=25, y = 0)
        tk.Label(matriz_paneles[meta[0] - 1][meta[1] - 1], text="Geppeto - META" ).place(x=25, y = 0)
        
        labelSolucion = "Camino Solución:  \n Meta "
        
        for i in profundidad.BusquedaProfundidadIterativa(inicio,meta,ambiente):
            x = i.estado_actual[0]
            y = i.estado_actual[1]
            labelSolucion = labelSolucion + "<- (" + str(i.estado_actual[0]) + ","+ str(i.estado_actual[1]) +  ") "
            
            labelCamino = tk.Label(matriz_paneles[x-1][y-1], text="P",bg="green")
            labelCamino.place(x = 40 , y =20)
            
        
        
        labelSolucion = labelSolucion + " <- Inicio"
        label = tk.Label(root, text=labelSolucion) 
        label.grid(row=1, column=0)

#Botones
boton_amplitud = tk.Button(panel_principal)
boton_amplitud.config(text="Amplitud", command= busqueda_amplitud)
boton_amplitud.grid(row=0, column= 2 )

boton_costo = tk.Button(panel_principal)
boton_costo.config(text="Costo", command=busqueda_costo)
boton_costo.grid(row=0, column= 3 )

boton_profundidad = tk.Button(panel_principal, command=busqueda_profundidad)
boton_profundidad.config(text="Profundidad")
boton_profundidad.grid(row=0, column= 4 )


def limpiarCampos():
    entrada_nodoInicio.delete(0, "end")
    entrada_nodoMeta.delete(0,"end")

boton_limpiar = tk.Button(panel_principal, command= lambda: limpiarCampos())
boton_limpiar.config(text="Limpiar campos")
boton_limpiar.grid(row=1, column= 2)

def reiniciar():
    obtenerEscenario()
    boton_amplitud.config(state="normal")
    boton_costo.config(state="normal")
    boton_profundidad.config(state = "normal")
    boton_nuevo_camino.config(state="disabled")
    
boton_nuevo_camino = tk.Button(panel_principal, command= reiniciar)
boton_nuevo_camino.config(text="Reiniciar", state="disabled")
boton_nuevo_camino.grid(row=1, column= 4)


obtenerEscenario()
root.mainloop()


