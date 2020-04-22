"""
    mostrar  todos los numero que esten entre los numeros que de el usuario
"""

num1 = int(input('Ingrese primer numero: '))
num2 = int(input('Ingrese segundo numero: '))

if num1<num2:
    for numero in range(num1,num2):
        print(numero)
elif num1>num2:
    for numero in range(num2,num1):
        print(numero)
