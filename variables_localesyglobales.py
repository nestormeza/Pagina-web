def holaMundo():
    frase = 'Hola mundo!'
    print("Dentro de la funcion")
    print(frase)

    year = 2019
    print(year)

    global website
    website = 'Nestor Rosas'

    print('Dentro :',website)

    return 'datos devuetlo '+ str(year)


print(holaMundo());
