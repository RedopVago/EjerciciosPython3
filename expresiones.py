import re
import sys

patron = '[0-9]{10}'

result = re.match(patron, '3322116655')


def suma(a, b):
    patron = '[0-9]*$'

    ra = re.match(patron, str(a))
    rb = re.match(patron, str(b))

    if ra and rb:
        return int(a)+int(b)
    else:
        print('Se deben ingresar numeros positivos')


# print(suma(3, 5))
# print(suma('3', 5))


# texto = 'Buen dia 19'
#

# f = open('C:\PV\Cinvestav\PadtsSeguridad202006\Clases\Python.txt', 'r')
# file = f.read() #\n
# # print(file)
# f. close()
# #
# # patron = '[Tt]he'
# # fa = re.findall(patron, file)
# # # print(fa)
# # print(len(fa))
#
# s = re.sub('[Pp]ython', '<<PYTHON>>', file)
# f = open('PYTHON.txt', 'w')
# f.write(s)
#
#
# sys.exit()
