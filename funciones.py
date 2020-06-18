
def primera():
    print('Hola a todos!')

### Parametros
def saludo(nombre):
    return 'Hola ' + nombre

# print(primera())
# print(saludo('Pedro'))


### Parametros por defecto
def hola(name='juan', lastname='Valenzuela'):
    print('Hola', name, lastname)

def hola2(*nombres):
    lista = list(nombres)
    lista[0] = 'jose'

    nombres = tuple(lista)
    print(nombres)

def hola4(**nombres):
    print(nombres)


### Parametros variables
# def varargs():


# hola()
# hola(lastname='perez')
# hola2('juan', 'valenzuela', 'hernandez')
# hola4(n=1, ln=True, ln2='hernandez')
# persona = {'nombre': 'juan', 'apellido': 'valenzuela'}
# hola4(**persona)
# tt = 'juan', 'valenzuela', 'hernandez'
# hola2(*tt)

apellido, ap2 = 'valenzuela', 'hernandez'

tmp = ap2
ap2= apellido
apellido = tmp

apellido, ap2 = (ap2, apellido)

print(apellido)
print(ap2)

