#Ejercicios en Python
#Ej1 (Básico hola mundo)
print("Hola mundo")
#Ej2 (Asignar variable)
mi_variable=15
print(mi_variable)
#Ej3 (Posición de una variable en el mostrar por pantalla)
precio_1=100
precio_2=120.5
print("Precio 1","%5d"%precio_1) # Ocupando 5 posiciones
print("Precio 1",precio_1)
print ("Precio 2","%8.2f"%precio_2) # Que reserve 8 espacios de los cuales 2 sean para decimales
print ("Precio 2",precio_2)
dato=5
print("%03d"%dato)
#Ej4 (Input string)
datoInput=input("Ingrese mensaje:") # datoInput quedará como tipo de dato string
print(datoInput)
#Ej5 (Convertir string a int/float)
numInt=int(input("Número entero:"))
numFloat=float(input("Número real:"))
print(numInt+numFloat)