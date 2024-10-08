#-------------------------------------------------------------------------------
# Name:        Clase 3
#
# Author:      Ariadna Villagra
#
# Created:     01/09/2024

#1. Implementar una función que calcule la suma de todos los números enteros comprendidos
#entre cero y un número entero positivo dado.
#2. Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia
#adelante.
#3. Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores.
#4. Dado un nro iniciar una cuenta regresiva por medio de una función recursiva, imprimir la
#cuenta y al llegar a cero imprimir por pantalla "¡Booom!".
#5. Escriba una función recursiva para contar en cuantos intentos se puede adivinar el número de
#un dado. Pasos a seguir:
#a. Genere un número random
#b. Solicite al usuario que ingrese un nro
#c. Verifique si es correcto informe que acertó en X intento
#d. Si no acertó, cuente el intento y vuelva a solicitar el nro

#-------------------------------------------------------------------------------
#Ejercicio 1
def sumatotal():
 num = int(input("Ingrese un número "))
 suma = 0
 for i in range (0, num+1):
  suma += i
 return suma

resultado = sumatotal()

print("La suma total es:", resultado)

#Ejercicio 2

vec = [10, 20, 30, 40]

def recursiva(imax):

 if imax < 0:
  return[]
 else:
    lista = recursiva(imax - 1)
    lista.insert(0,vec[imax])
    return lista

lista = recursiva(len(vec) - 1)
print("La lista es", lista)

#Ejercicio 3
lista=0
a= [[23,45,63],[72,81,91],[56,64,37],[34,75,26]]

def conteo(imax):

 if imax < 0:
  return[]
 else:
    lista = conteo(imax - 1)
    lista.append(a[imax])
    return lista

lista = conteo(len(a) - 1)
print(lista)

#Ejercicio 4

numero= 0
numero = int(input("Ingrese un numero "))
def bomba(numero):

 if numero < 0:
  return "BOOM"
 else:
  print(numero)
  return bomba(numero - 1)

resultado = bomba(numero)
print(resultado)

#Ejercicio 5
import random
numero_aleatorio = random.randint(1,6)

def dado(intento=1):

 numero = int(input("Ingrese un numero "))
 if numero == numero_aleatorio:
  return f"SIII NUMERO CORRECTO,en el intento {intento}"
 else:
  print("nooo,ingrese otro numero")

  return dado(intento+1)

resultado = dado()
print(resultado)


