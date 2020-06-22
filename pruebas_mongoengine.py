from mongoengine import *

import datetime

connect('mongoenginedb')


# Esquema/Modelo
class Persona(Document):
    nombre = StringField(required=True)
    # fecha = DateTimeField(required=True)
    fecha = StringField(required=True)
    lugar = StringField(required=True)


# persona = Persona(
#     nombre='Pedro',
#     fecha='1985/11/04',
#     lugar='Sonora'
# )

# # persona.save()
# print(f'_id: {persona.id}\nNombre: {persona.nombre}')
#
# persona.nombre = 'Juan'
# persona.save()
# print(f'_id: {persona.id}\nNombre: {persona.nombre}')

nombres = ['ana', 'maria', 'jose']
fechas = ['2000/02/23', '1952/08/12', '1997/12/07']
lugares = ['Jalisco', 'Colima', 'Nayarit']

# for n, f, l in zip(nombres, fechas, lugares):
#     tmp = Persona(nombre=n, fecha=f, lugar=l)
#     tmp.save()

personas = Persona.objects

for index, p in enumerate(personas):
    print(f'{index+1} - Nombre: {p.nombre}\nLugar: {p.lugar}\nFecha: {p.fecha}')

pass