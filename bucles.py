numero = int(input('ingrese un numero: '))
print('####### for #######')
for x in range(0,13):
    print('{} * {} = {}'.format(numero,x,numero*x))

print('###### while #####')
contador=0
while contador <= 100:
    print('{}'.format(contador))
    contador += 1
