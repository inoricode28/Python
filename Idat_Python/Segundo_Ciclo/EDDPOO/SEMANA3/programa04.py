from tkinter import *
ventana = Tk()
ventana.title("Mi ventana")
ventana.geometry("750x200")
ventana.configure(background="green")


etiqueta = Label(ventana,text="Hola", font = ("Arial Bold",20))
etiqueta.grid(row = 0, column = 0) 

def click():
    etiqueta.configure(text = "Hiciste click en el boton...!!!")

boton = Button(ventana,text="Click aqui", bg = "orange", fg= "red",command=click)
boton.grid(row=0, column=1)


texto = Entry(ventana,width=20)
texto.grid(row = 0, column=2)


ventana.mainloop()