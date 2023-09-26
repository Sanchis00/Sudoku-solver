'''Programa encargado de resolver sudokus creados por el usuario mediante
Back-Testing (fuerza bruta)'''


from tkinter import *
from resolutor import solver

screen = Tk()
screen.title("Resolutor de Sudoku")
screen.geometry("424x550")

tutorial = Label(screen,text="Completa los números y dale click a 'Resolver'",font=("Helvetica",11))
tutorial.grid(row=0,column=1,columnspan=10,padx=8)

acierto = Label(screen,text="",fg="green")
acierto.grid(row=15,column=1,columnspan=10,pady=5)
error = Label(screen,text ="",fg="red")
error.grid(row=15,column=1,columnspan=10,pady=5)


celdas = {}


def ValidarNumero(n):
    '''Comprueba que el caracter introducido en la casilla sea
    un numero del 1 al 9, de lo contrario no permite su introducción'''
    comprobar = (n.isdigit() or n =="") and len(n) < 2
    return comprobar

registrar = screen.register(ValidarNumero)

def draw3x3(fila,columna,bgc):
    '''Funcion encargada de rellenar las celdas'''
    for x in range(3):
        for y in range(3):
            e = Entry(screen, width = 5, bg= bgc,justify="center",validate="key",validatecommand=(registrar,"%P"))
            e.grid(row = fila + x+1, column = columna + y+1, sticky = "nsew",padx=1,pady=1,ipady = 5,ipadx=5)
            celdas[(fila + x + 1,columna + y+1)] =e


def draw9x9():
    '''Funcion principal que, gracias a la funcion anterior,
    se encarga de rellenar el sudoku al completo. También es la encargada
    de colorear las casillas'''
    color = "white"
    for rowNum in range(1,10,3):
        for colNum in range(0,9,3):
            draw3x3(rowNum,colNum,color)
            if color == "white":
                color = "lightblue"
            else:
                color = "white"

def limpiar():
    '''Funcion encargada de borrar el tablero y las etiquetas'''
    error.configure(text="")
    acierto.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            celda = celdas[(row,col)]
            celda.delete(0,'end')

def inputUsuario():
    '''Funcion que procesa el input del usuario'''
    tablero = []
    error.configure(text="")
    acierto.configure(text="")
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            valor = celdas[(row,col)].get()
            if valor == "":
                rows.append(0)
            else:
                rows.append(int(valor))

        tablero.append(rows)
    updateValues(tablero)




b_resolver = Button(screen,command=inputUsuario,text="Resolver",width = 10)
b_resolver.grid(row=20,column=1,columnspan=5,pady=20)


b_borrar = Button(screen,command=limpiar,text="Borrar",width = 10)
b_borrar.grid(row=20,column=5,columnspan=5,pady=20)

def updateValues(solucion):
    '''Funcion que se encarga de mostrar los valores en el tablero
    unicamente si el sudoku se ha completado sin errores. En tal caso,
    habilitará la etiqueta de "Sudoku resuelto". De lo contrario, habilitará
    una etiqueta para informar de que el sudoku no tiene solución.'''
    sol = solver(solucion)
    if sol!= "No":
        for row in range (2,11):
            for col in range(1,10):
                celdas[(row,col)].delete(0,"end")
                celdas[(row,col)].insert(0,sol[row-2][col-1])
            acierto.configure(text="Sudoku Solved")
    else:
        error.configure(text="No tiene solución")



draw9x9()
screen.mainloop()