#1)
nombre=input("Ingrese su nombre:")
print("¡Hola",nombre+"!")

#2)
num=int(input("Ingrese un número para calcular la cuarta parte: "))
print(num/4)

#3) 
nota1=float(input("Ingrese nota de Taller de programación I: "))
nota2=float(input("Ingrese nota de Administración empresarial II: "))
nota3=float(input("Ingrese nota de Marketing: "))
print("Su promedio fue de:",(nota1+nota2+nota3)/3)

#4)
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
print("La suma de estos dos número es:",num1+num2)
print("La diferencia entre estos dos números es:",num1-num2)

#5)
factura=float(input("Ingrese el monto de la factura en $: "))
iva=(21*factura)/100
print("El monto total más el IVA es de:$",factura+iva)

#6)
ausentes=int(input("¿Cuantas personas se ausentaron en el día? "))
while ausentes < 0 or ausentes > 70:
    print("Indique un número de personas coherente")
    ausentes=int(input("¿Cuantas personas se ausentaron en el día? "))
porcentajeAusentes=(ausentes*100)/70
porcentajeAusentesSTR=str(porcentajeAusentes)
print(porcentajeAusentesSTR+"% es el porcentaje de ausentes")

#7
medidaMetros=float(input("Ingrese la medida en metros: "))
medidaCm=medidaMetros*100
print("Su medida en centimetros:",medidaCm)
medidaPulgada=medidaCm/2.54
print("Su medida en pulgadas es:",medidaPulgada)
medidaPie=medidaPulgada/12
print("Su medida en pies es:",medidaPie)
medidaYarda=medidaPie/3
print("Su medida en yardas es:",medidaYarda)

#8
nVendedor=int(input("Ingresar número del vendedor: "))
salarioBase=250
comisionPorVenta=40
porcientoFinal=0
ventasRealizadas=int(input("Ingresar ventas realizadas: "))
comisionFinal=ventasRealizadas*comisionPorVenta
for i in range(ventasRealizadas):
    venta=float(input("Valor de la venta: "))
    porcientoDeVenta=(venta*5)/100
    porcientoFinal=porcientoFinal+porcientoDeVenta
salarioTotal=salarioBase+comisionFinal+porcientoFinal
print("Al vendedor con número:",nVendedor,"le corresponde un salario de:",salarioTotal,"pesos")

#9
dineroInvertido=float(input("¿Cuanto dinero quiere invertir? "))
pagaMensual=0
for i in range(6):
 plazo=(dineroInvertido*2)/100
 pagaMensual=pagaMensual+plazo
print("En seis meses, usted ganará $",pagaMensual)

#10
sueldo=float(input("¿Cuanto gana como odontólogo?"))
impuestosNacionales=(sueldo*5)/100
colegio=(sueldo*2)/100
municipio=(sueldo*0.3)/100
total=impuestosNacionales+colegio+municipio
print("El impuesto nacional que debe pagar es $",impuestosNacionales,
      "Lo que debe pagar del colegio es $",colegio,
      "Y lo adeudado del municipio es $",municipio,
      "Dando un total de $",total)

#11
horasTrabajadas=int(input("Ingresar total de horas trabajadas "))
sueldoxHora=500
sueldoBruto=horasTrabajadas*sueldoxHora
jubilacion=(sueldoBruto*11)/100
print("Descuento de jubilación: $",jubilacion)
obraSocial=(sueldoBruto*3)/100
print("Descuento de obra social: $",obraSocial)
cuotaSindical=(sueldoBruto*2)/100
print("Descuento de cuota sindical: $",cuotaSindical)
sueldoTotal=sueldoBruto-jubilacion-cuotaSindical-obraSocial
print("El sueldo total a cobrar es de: $",sueldoTotal)

#12
valorArticulo=float(input("Ingresar el valor del artículo "))
descuento=int(input("Ingresar el porcentaje de descuento del artículo "))
descuentoAplicado=(valorArticulo*descuento)/100
precioFinal=valorArticulo-descuentoAplicado
print("El precio final del artículo es de: $",precioFinal)