# una variable almacena un valors
texto = 'Master del curso de python'
texto2 = 'con Nestor Rosas'
num = 10
decimal = 35.6
lista = [2,3,4,5]
tupla = ('nombre','Nestor') #las duplas no cambias
diccionario = {
    'Nombre' : 'Nestor',
    'Apellidos' : 'Rosas'
}
rango = range(9) # rango de numeros
boolean = False

#imprimir datos
print(texto)
print(texto2)
print(num)
print(decimal)
print(lista)
print(tupla)
print(diccionario)
print(rango)
print(boolean)

#concatenar
print(texto+' '+texto2)
print('hola {} + {}'.format(texto,texto2))
# print(f'{texto}')

#saber el tipo de datos
print(type(texto))

#convertir  tipo de datos
numero = str(54)
print ('concatenar {} {}'.format(texto,numero))
