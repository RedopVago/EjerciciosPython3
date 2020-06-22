import re

# Correo electronico
correos = 'j.pedro@padts.mx', 'j.pedro@padts.com.mx', 'j.pedro@python.padts.com'


pc = '[a-zA-Z0-9._]{5,10}@[a-zA-Z0-9]*(\.[a-zA-Z0-9]*)?(\.[a-zA-Z0-9]{2,3}){1,2}$'

print('Verificacion de correos:')
for c in correos:
    print(f'{c} passes' if re.match(pc, c) else f'{c} fails')


# Numero Telefonico
pt = '[0-9]{10}|\([0-9]{2,3}\)[0-9]{7,8}|\([0-9]{2,3}\)[ -]?[0-9]{3,4}[ -]?[0-9]{4}$'

tels = '3316054756', '(33)16054756', '(331)6054756', '(33) 1605 4756', \
       '(331) 605 4756', '(33) 1605-4756', '(331) 605-4756'

print('\nVerificación de telefonos:')
for t in tels:
    rt = re.match(pt, t)
    if rt:
        print(f'{t} passes')
    else:
        print(f'{t} fails')


# RFC
rfc = 'VAGJ851104MJ8', 'FIRB810824MSPGSR07'

for r in rfc:
    print(f'{r} passes' if re.match('[A-Z]{4}[0-9]{6}[A-Z0-9]{5}[A-Z0-9]{2}$', r) else f'{r} fails')


curp = 'VAGJ851104HSRLDN04', 'FIRB810824MSPGSR07'

for c in curp:
    print(f'{c} passes' if re.match('[A-Z]{4}[0-9]{6}[HM][A-Z]{3}', c) else f'{c} fails')