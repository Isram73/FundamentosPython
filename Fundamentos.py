def nuevoTema(tema):
    print("\n========", tema, "=========\n")

#Este es un comentario de una linea
nuevoTema("Operador aritmetico")

print("Operador division entera (10//3): ", 10//3)
print("Operador potencia (5 ** 3): ", 5**3) #Operador **

'''Este es un
comentario de 
varias lineas'''

nuevoTema("Operadores logicos")
print("Operador and (True and False): ", True and False) #True y False siempre van con mayuscula

#Actividad: Imprimir la tabla de verdad de los operadores logicos
print()
print("==== Operador and ====")
print("Operador and (True and True): ", True and True)
print("Operador and (True and False): ", True and False)
print("Operador and (False and True): ", False and True)
print("Operador and (False and False): ", False and False)
print("==== Operador or ====")
print("Operador or (True or True): ", True or True)
print("Operador or (True or False): ", True or False)
print("Operador or (False or True): ", False or True)
print("Operador or (False or False): ", False or False)
print("==== Operador not ====")
print("Operador not (not True): ", not True)
print("Operador not (not False): ", not False)

#Operadores de comparaci�n
nuevoTema("Operadores de comparacion")
print("2 == 3", 2 == 3)
#Actividad: Agregar los dem�s operadores de programaci�n
print()
print("3 != 7", 3 != 7)
print("3 < 7", 3 < 7)
print("3 <= 7", 3 <= 7)
print("3 > 7", 3 > 7)
print("3 >= 7", 3 >= 7)

nuevoTema("Variables")
variable1 = 10
_variable2 = 6.2456
Variable3 = "Juancho"
dosPalabras = "Hola"
dos_palabras = "Hello"

print(variable1, _variable2, Variable3, dosPalabras, dos_palabras)

a, b, c = 10, 5.16, "Palabra"
print(a, b, c)

nuevoTema("Enteros")
w = 105
x = 982497927612
y = -256
z = 0b00110011
h = 0xffa

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

nuevoTema("Flotantes")
x = 1297.50
print (x, type(x))
y = 0.5637939
print(y, type(y))

nuevoTema("Numeros complejos")
x = -46j
y = 12 + 45j
z = 2j
print(x, type(x))
print(y, type(y))
print(z, type(z))

nuevoTema("Booleanos")
lis = [8]
print (lis, "es", bool(lis))
t = ()
print(t, "es", bool(t))
new = "Hello"
print(new, "es", bool(new))
num = 99
print(num, "es", bool(num))
comp = 1 + 0j
print(comp, "es", bool(comp))
val = None #None equivale a NULL
print(val, "es", bool(val))

nuevoTema("Listas") #No son arreglos
a = [10, 20.5, "Python list"]
print(a)
print(a[1])
a[0] = "Hola"
print(a)

nuevoTema("Tuplas")
t = (25, "Tupla", 1 + 10j, 3.1416)
print(t)
print(t[2])
print("t[0:2]", t[0:2]) #El "[0:2]" es un rango, y es del 0 al 2-1
print("t[0:4]", t[0:4])
#t[1] = 34, Operacion no valida en Tuplas

nuevoTema("Conjuntos") #Los conjuntos son únicos, no se pueden repetir valores
t = {50, 20, 30, 40, 10, 50}
print("Conjunto t=", t, type(t))

nuevoTema("Diccionario")
d = {1:"Valor1", 
       "Valor2":2j}
print(d, type(d))
print("d[Valor2]:", d["Valor2"])

nuevoTema("Cadenas")
cadena1 = "Cadena con comillas dobles"
cadena2 = 'Cadena con comillas simples'

print(cadena1, type(cadena1))
print(cadena2, type(cadena2))

cadenaMultilinea = '''Esta es una cadena
de varias lineas   con    tabulares  y
saltos
de
linea\n'''

print(cadenaMultilinea)
print("'Segmentacion de cadenas'")
print(cadena1)
print(cadena1[5:11])
print(cadena1[:5])
print(cadena1[7:])
print(cadena1[-8:-1])
print(cadena1[0:18:1])
print(cadena1[0:18:2])
print(cadena1[0:18:3])

print()
cadena1 = "Hola"
cadena4 = (cadena1 + " ") * 5
print(cadena4)
cadena5 = cadena4.capitalize()
print(cadena5)