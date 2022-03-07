A = float(input("Primer Valor: \n -->"))
B= float(input("Segundo Valor: \n -->"))

#Realizar el calculo
S=A+B
R=A-B
M=A*B
D=A/B

#print("Resultados de la suma es %f"%(S)) //define tipo decimal
#print("Resultados de la suma es %d"%(S)) //Define tipo Entero
print("Resultado de la suma es {:.0f}".format(S))
print("Resultado de la resta es {:.0f}".format(R))
print("Resultado de la Multiplicacion es {:.0f}".format(M))
print("Resultado de la divicion es {:.1f}".format(D))



