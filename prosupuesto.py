print("ingrese el precio de el paquete de frutas")
fruta = int(input ())
print("ingrese el precio de el paquete de verduras")
verduras = int(input ())
print("ingrese el precio de el paquete de granos")
granos = int(input ())
print ("ingrese el presupuesto")
presupuestos = int(input())
print ("los precios de los productos son", presupuestos)
def funcion(a,b,c):
  if(((a-3) + (b-2) + (c-5)) < presupuestos):
      print("Es un buen comprador")
  elif (((a-3) + (b-2) + (c-5))== presupuestos):
      print("Está a su limite de presupuesto")
  else:
     print("Regrese pronto")
     


