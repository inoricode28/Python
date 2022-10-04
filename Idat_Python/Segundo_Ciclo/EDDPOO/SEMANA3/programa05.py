from tkinter import *
from tkinter import messagebox
ventana = Tk()
ventana.title("Mi Calculadora")
ventana.geometry("380x220")
ventana.configure(background="yellow")

etiqueta01 = Label(ventana,text="Primer Numero", font = ("Arial Bold",15),bg="yellow")
etiqueta01.grid(row = 0, column = 0) 

etiqueta02 = Label(ventana,text="Segundo numero", font = ("Arial Bold",15),bg="yellow")
etiqueta02.grid(row = 1, column = 0) 
texto01 = Entry(ventana,font = ("Arial Bold",15),justify=CENTER)
texto01.grid(row = 0, column=1)

texto02 = Entry(ventana,font = ("Arial Bold",15),justify=CENTER)
texto02.grid(row = 1, column=1)
#Variable para almacenar los resultados
resultado= StringVar()
#Creamos funciones

def suma():
    suma = int(texto01.get())+ int(texto02.get())
    return resultado.set(suma)
def resta():
    resta = int(texto01.get()) - int(texto02.get())
    return resultado.set(resta)

def Multipliacion():
    multiplicacion = int(texto01.get()) * int(texto02.get())
    return resultado.set(multiplicacion)
    

def Divicion():
    try:
        divicion = int(texto01.get()) / int(texto02.get())
        return resultado.set(divicion)
    except ZeroDivisionError:
        messagebox.showinfo(title= "ERROR", message="No se puede dividir entre 0....!!!!!")
        texto01.delete(0,END)
        texto02.delete(0,END)
        texto01.focus()

def Cerrar():
    ventana.destroy()

#creamos nuestro botontes
boton_suma = Button(ventana, text = "+", bg = "green", fg = "white",width=10,font = ("Arial Bold",15), command = suma)
boton_suma.grid(row=2, column=0)

boton_resta = Button(ventana, text = "-", bg = "green", fg = "white",width=10,font = ("Arial Bold",15), command = resta)
boton_resta.grid(row=2, column=1)

boton_Multiplicacion = Button(ventana, text = "^", bg = "green", fg = "white",width=10,font = ("Arial Bold",15), command = Multipliacion)
boton_Multiplicacion.grid(row=3, column=0)

boton_Dividir = Button(ventana, text = "/", bg = "green", fg = "white",width=10,font = ("Arial Bold",15), command = Divicion)
boton_Dividir.grid(row=3, column=1)

boton_cerrar = Button(ventana, text = "Cerrar", bg = "gray", fg = "white",width=33,font = ("Arial Bold",15), command = Cerrar)
boton_cerrar.grid(row=4, column=0, columnspan=2)

etiqueta03 = Label(ventana, bg="white",width=33,fg="black", font = ("Arial Bold",15),textvariable=resultado)
etiqueta03.grid(row = 5, column = 0,columnspan=2)


ventana.mainloop()