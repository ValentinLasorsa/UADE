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
print((nota1+nota2+nota3)/3)

#4)
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
print("La suma de estos dos número es:",num1+num2)
print("La diferencia entre estos dos números es:",num1-num2)

#5)
factura=float(input("Ingrese el monto de la factura en $: "))
iva=(21*factura)/100
print("El monto total más el IVA es de:$"+factura+iva)

#6)
ausentes=int(input("¿Cuantas personas se ausentaron en el día? "))
while ausentes < 0 or ausentes > 70:
    print("Indique un número de personas coherente")
    ausentes=int(input("¿Cuantas personas se ausentaron en el día? "))
porcentajeAusentes=(ausentes*100)//70
porcentajeAusentesSTR=str(porcentajeAusentes)
print(porcentajeAusentesSTR+"% es el porcentaje de ausentes")

#7
