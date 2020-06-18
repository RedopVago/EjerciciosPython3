import re

# No letras
nl = '[^a-zA-Z]$'
print('No letras:', True if re.match(nl, texto) else False)

# Solo Numeros
sn = '\d+$'
print('Solo numeros:', True if re.match(sn, texto) else False)

# Solo mayusculas
sM = '[A-Z]+$'
print('Solo mayusculas:', True if re.match(sM, texto) else False)


# Solo minusculas
sm = '[a-z]+'
print('Solo minusculas:', True if re.match(sm, texto) else False)


# No numeros
nn = '[^0-9]$'
print('No numeros:', True if re.match(nn, texto) else False)