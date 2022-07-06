"""
  Se tiene una Lista donde se almacena las ventas mensuales de 
  una empresa. visualice:
  a) El mes que se dieron las ventas  máximas
  b) ¿a cuánto ascendieron las ventas máximas?
  c) El total de las ventas
  d) El promedio de ventas
"""

from random import randint

ventas = [[] for x in range(12)]

meses = [
  "Ene", 
  "Feb", 
  "Mar", 
  "Abr", 
  "May", 
  "Jun", 
  "Jul", 
  "Ago", 
  "Sep",
  "Oct",
  "Nov",
  "Dic"
]

total_ventas = 0
promedio_ventas = 0
counter_ventas = 0
mes_max_ventas = ""
mes_max_ventas_total = 0

for (index, value) in enumerate(ventas):
  ventas[index] = { "mes": "", "total": 0, "data": [] }
  ventas[index]["data"] = [randint(10, 3000) for x in range(randint(1, 10))]
  ventas[index]["total"] = sum(ventas[index]["data"])
  ventas[index]["mes"] = meses[index]
  counter_ventas += len(ventas[index]["data"])
  total_ventas += ventas[index]["total"]
  
print("==============================")
print("  Ventas mensuales")
print("==============================")
for (index, venta) in enumerate(ventas):
  counter = len(venta['data'])
  print(f" {venta['mes']} ", end="")
  print(f" => {counter} ventas; S./ {venta['total']}")
print("==============================")

# total maximo
arr_total_ventas = [venta["total"]  for venta in ventas]
mes_max_ventas_total = max(arr_total_ventas)
# mes maximo
index_mes_max = arr_total_ventas.index(mes_max_ventas_total)
mes_max_ventas = meses[index_mes_max]
# promedio de ventas
promedio_ventas = round(total_ventas / counter_ventas, 2)

print(f"a) El mes que se dierón las ventas máximas: {mes_max_ventas}")
print(f"b) Las ventas máximas ascendieron a: S./ {mes_max_ventas_total}")
print(f"c) El total de ventas es: S./ {total_ventas}")
print(f"d) El promedio de ventas es: S./ {promedio_ventas}")