import serial
import time
from tkinter import*
#color="#00878F"
color="#00248f"

arduino = serial.Serial('COM4',9600)
time.sleep(2)

def foco1():
	arduino.write('a'.encode())#pin2

def foco2():
	arduino.write('s'.encode())#pin3

def foco3():
	arduino.write('d'.encode())#pin4	

def foco4(): 
	arduino.write('f'.encode())#pin3	

def foco5():
	arduino.write('g'.encode())#pin4

def foco6():
	arduino.write('h'.encode())#pin5

def foco7():
	arduino.write('j'.encode())#pin6

def foco8():
	arduino.write('k'.encode())#pin7

def foco9():
	arduino.write('l'.encode())#pin8

def foco10():
	arduino.write('z'.encode())#pin9

def foco11():
	arduino.write('x'.encode())#pin10

def foco12():
	arduino.write('c'.encode())#pin11

def cerrar():
	arduino.close()
	ventana.destroy()


ventana=Tk()
Label(ventana,text="PRO-PYTHON",bg=color,fg=("#ede60c"),font=("Times New Roman",12)).place(x=48,y=10)
ventana.configure(background=color)
ventana.title("Casa Domotica con Arduino")
ox,oy=ventana.winfo_screenwidth()/2,ventana.winfo_screenheight()/2
ventana.geometry("200x550+%d+%d"% (ox-200,oy-100))
ventana.wm_deiconify()
ventana.iconbitmap("jk.ico")
#ventana.geometry('350x200')
#label=Label(ventana,text="")
#label.grid(row=1,column=1)
#35A8CC
b1=Button(ventana,text="Prende/Apaga FOCO1",font=("Comic Sans MS",10),command=foco1,bg='#C9DB2C')
b1.place(x=28,y=40)
b2=Button(ventana,text="Prende/Apaga FOCO2",font=("Comic Sans MS",10),command=foco2,bg='#C9DB2C')
b2.place(x=28,y=80)
b3=Button(ventana,text="Prende/Apaga FOCO3",font=("Comic Sans MS",10),command=foco3,bg='#C9DB2C')
b3.place(x=28,y=120)
b4=Button(ventana,text="Prende/Apaga FOCO4",font=("Comic Sans MS",10),command=foco4,bg='#C9DB2C')
b4.place(x=28,y=160)
b5=Button(ventana,text="Prende/Apaga FOCO5",font=("Comic Sans MS",10),command=foco5,bg='#C9DB2C')                         
b5.place(x=28,y=200)
b6=Button(ventana,text="Prende/Apaga FOCO6",font=("Comic Sans MS",10),command=foco6,bg='#C9DB2C')
b6.place(x=28,y=240)
b7=Button(ventana,text="Prende/Apaga FOCO7",font=("Comic Sans MS",10),command=foco7,bg='#C9DB2C')
b7.place(x=28,y=280)
b8=Button(ventana,text="Prende/Apaga FOCO8",font=("Comic Sans MS",10),command=foco8,bg='#C9DB2C')
b8.place(x=28,y=320)
b9=Button(ventana,text="Prende/Apaga FOCO9",font=("Comic Sans MS",10),command=foco9,bg='#C9DB2C')
b9.place(x=28,y=360)
b10=Button(ventana,text="Prende/Apaga FOC10",font=("Comic Sans MS",10),command=foco10,bg='#C9DB2C')
b10.place(x=28,y=400)
b11=Button(ventana,text="Prende/Apaga FOC11",font=("Comic Sans MS",10),command=foco11,bg='#C9DB2C')
b11.place(x=28,y=440)
#b1=Button(ventana,text="Prende/Apaga led",command=led)
#b1.grid(row=0,column=0)
#b2=Button(ventana,text="Actualizar valor",command=potenciometro)
#b2.grid(row=1,column=0)
#b3=Button(ventana,text="Cerrar",command=cerrar)
#b3.grid(row=2,column=0)
b13=Button(ventana,text="Cerrar",font=("Comic Sans MS",10),command=cerrar,bg='#FAED1F')
b13.place(x=70,y=480)
ventana.mainloop()