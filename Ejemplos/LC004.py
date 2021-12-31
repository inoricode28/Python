Alumno=input("Identificacion del alumno: \n -->")
Curso=input("Nombre del curso: \n -->")
Practica=int(input("Promedio de practicas: \n -->"))
Parcial=int(input("Examen parcial: \n -->"))
Final=int(input("Examen final: \n -->"))
##Realizar calculos
Promedio=float(((Practica*2)+(Parcial*1)+(Final*3))/6)
print ("Promedio Final es %f"%(Promedio))