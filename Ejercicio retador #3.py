Cemento_peso=40
Yeso_peso=30
maximo_de_carga=3254
costales_cemento=int(input("Numero de costales de cemento (kg) "))
costales_yeso=int(input("Numero de costales de yeso (kg) "))
peso_total=(Cemento_peso*costales_cemento)+(Yeso_peso*costales_yeso)

confirmacion_envio=peso_total>(maximo_de_carga/2) and peso_total<=maximo_de_carga

print("El peso total en kg es:",peso_total)
print("¿Se puede realizar el envio? ",confirmacion_envio)
