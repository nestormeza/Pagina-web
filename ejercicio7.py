num1 = int(input('Ingrese primer numero: '))
num2 = int(input('Ingrese segundo numero: '))

if num1<num2:
    for numero in range(num1,num2):
        if numero%2 != 0:
            print(numero)
elif num1>num2:
    for numero in range(num2,num1):
        if numero%2 != 0:
            print(numero)  
