producto=""
costo_caja=0
costo_total=0
numero_cajas=int(input("Numero de cajas a vender: "))
id_producto=int(input ("Id de producto: "))
if numero_cajas<=100:
 if id_producto==1:
  producto="Maíz grano"
  costo_caja=285.55
 elif id_producto==2:
  producto="Pepino"
  costo_caja=334.72
 elif id_producto==3:
  producto="Tomate verde"
  costo_caja=129.0
else:
  print("No se puede realizar la venta a mas de 100 unidades")

costo_total=(numero_cajas*costo_caja)+1500
print("El producto es: ",producto,"\n","El precio por caja es: ",costo_caja,"\n","El costo total a pagar:",costo_total)
