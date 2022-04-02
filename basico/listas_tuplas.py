# Es dinamico las listas mutable
objetos = ["Hola", 3, 4.5, True]
print (objetos)

objetos.append(False)

objetos.append(7)
objetos.pop(4)

for elemento in objetos:
    print(elemento)

print(objetos[::-1])
print(objetos[1:3])


numeros1 = [1, 2, 3, 4, 5, 6, 7]
numeros2 = [8, 9, 10]

numeros = numeros1 + numeros2
print (numeros * 7)

#Es estatico las tuplas inmutable
mi_tupla = (1 , 2, 3, 4, 5, 6, 7)

#no se puede usar append y pop
for numero in mi_tupla:
    print(numero)

