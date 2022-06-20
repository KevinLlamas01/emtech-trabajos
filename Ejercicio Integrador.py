producto=""
costo_caja=0
costo_total=0
suma_total=0
descuento=False
venta_productos = [[2, 122], [1, 89], [1, 22], [3, 48], [1, 75],[3, 322],[2, 95],[1, 148],[1, 83],[3, 100]]
for i in venta_productos:
  suma_total+=i[1]


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
suma_total+=numero_cajas
costo_total=(numero_cajas*costo_caja)+1500
if(suma_total<=1500):
  costo_total=(costo_total-((costo_total*20)/100))
  descuento=True

print("El producto es: ",producto,"\n","El precio por caja es: ",costo_caja,"\n","Aplica descuento del %20:",descuento,"\n","El costo total a pagar:",costo_total)
