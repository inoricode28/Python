from tkinter import *

ventana = Tk()
ventana.title("DATOS PERSONALES")
ventana.iconbitmap("dog.ico")
ventana.geometry("340x290")
ventana.configure(background = "black")

etiquetaTitulo = Label(ventana, text = "DATOS PERSONALES", bg = "black", fg = "white", font = ("Arial Bold", 16),justify = CENTER)
etiquetaTitulo.grid(row = 1, column = 1, columnspan = 2)

eti0 = Label(ventana, bg = "black", fg = "black", width = 33, font = ("Arial Bold", 5))
eti0.grid(row = 2, column = 1, columnspan = 2)

eti1 = Label(ventana, text = "Primer nombre", bg= "black", fg = "white", font = ("Arial Bold", 12))
eti1.grid(row = 3, column = 1)
eti1.config(padx = 5, pady = 5)

eti2 = Label(ventana, text = "Segundo nombre", bg = "black", fg = "white", font = ("Arial Bold", 12))
eti2.grid(row = 4, column = 1)
eti2.config(padx = 5, pady = 5)

eti3 = Label(ventana, text = "Primer apellido", bg = "black", fg = "white", font = ("Arial Bold", 12))
eti3.grid(row = 5, column = 1)
eti3.config(padx = 5, pady = 5)

eti4 = Label(ventana, text = "Segundo apellido", bg = "black", fg = "white", font = ("Arial Bold", 12))
eti4.grid(row = 6, column = 1)
eti4.config(padx = 5, pady = 5)

text1 = Entry(ventana, font = ("Arial Bold", 13),justify = CENTER)
text1.grid(row = 3, column = 2)

text2 = Entry(ventana, font = ("Arial Bold", 13),justify = CENTER)
text2.grid(row = 4, column = 2)

text3 = Entry(ventana, font = ("Arial Bold", 13),justify = CENTER)
text3.grid(row = 5, column = 2)

text4 = Entry(ventana, font = ("Arial Bold", 13),justify = CENTER)
text4.grid(row = 6, column = 2)

eti5 = Label(ventana, bg = "black", fg = "black", width = 33, font = ("Arial Bold", 5), justify = CENTER)
eti5.grid(row = 7, column = 1, columnspan = 2)

textVacio = Label(ventana, bg = "gray", fg = "black", width = 27, font = ("Arial Bold", 14), justify = CENTER)
textVacio.grid(row = 8, column = 1, columnspan = 2)

eti6 = Label(ventana, bg = "black", fg = "black", width = 34, font = ("Arial Bold", 8), justify = CENTER)
eti6.grid(row = 9, column = 1, columnspan = 2)

btn01 = Button(ventana, text = "Aceptar", bg = "black",fg = "white",width=10,height=1, font = ("Arial Bold", 15))
btn01.grid(row = 10, column = 1)

btn02= Button(ventana, text = "Limpiar", bg = "black",fg = "white",width=10,height=1, font = ("Arial Bold", 15))
btn02.grid(row = 10, column = 2)
 
ventana.mainloop()