
import sys
import time


def esPrimo(numero, n=2):
    """Funciono para validar si un numero es primo de forma recursiva"""

    if numero == n:
        return True

    if n < 2:
        return False

    if numero % n:
        return esPrimo(numero, n+1)
    else:
        return False


def isPrime(numero):
    """Funcion para validar si un numero es primo de forma iterativa"""
    if numero < 2:
        return False

    for n in range(2, numero):
        if not numero % n:
            return False

    return True


def ejercicios(i):
    if i > 0:
        s = 'El numero es positivo'
    elif i < 0:
        s = 'El numero es negativo'
    else:
        s = 'El numero es cero'

    print(s)

    if i%2:
        p = 'El numero es impar'
    else:
        p = 'El numero es par'

    print(p)


    if esPrimo(i):
        primo = 'El numero es primo'
    else:
        primo = 'El numero NO es primo'
    print(primo)


if __name__ == '__main__':
    print('Ingresa un numero:')
    try:
        inp = int(input())
    except ValueError:
        print('El dato ingresado no es un entero!', file=sys.stderr)
        sys.exit()

    ejercicios(inp)

    print('\nIngresa un año:')
    a = int(input())

    if a < 0:
        print('No se admiten años antes de cristo!')
        sys.exit()

    if a % 4:
        print(a, 'NO es un año bisiesto')
    elif a % 100:
        print(a, 'es un año bisiesto')
    elif a % 400:
        print(a, 'NO es un año bisiesto')
    else:
        print(a, 'es un año bisiesto')
