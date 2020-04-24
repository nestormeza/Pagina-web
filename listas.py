milista = ['Nestor','Rosas','Meza']

print(milista)
print(milista[1])

milista[1] ='Manuel'

print(milista[1])

milista.append('nuevo')
print(milista)

for lista in milista:
    print('{}. {}'.format(milista.index(lista)+1,lista))
