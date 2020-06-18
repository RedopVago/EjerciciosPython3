# read()
# readline()
# write()


def escribirArchivo(archivo, txt):
    t = txt.encode()
    archivo.write(t)


def leerArchivo(archivo):
    return archivo.read()


if __name__ == '__main__':
    file = open('pruebas2.txt', 'ab')
    txt = 'Esta es uan prueba de escritura a un archivo PYTHON\n'
    escribirArchivo(file, txt)
    file.close()
    #
    # file = open('pruebas.txt', 'r+')
    # l = leerArchivo(file)
    # print(l)
    #
    # txt2 = 'Escritura de un archivo abierto en mode r+\n'
    # file.write(txt2)
    # file.close()
    #
    file = open('pruebas.txt', 'rb')
    # print('\nSegunda lectura')
    l2 = leerArchivo(file)
    print(l2)
    file.close()

    print('leido:' + l2)






