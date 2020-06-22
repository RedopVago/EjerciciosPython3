from pymongo import MongoClient

def persona(nombre, fechaNacimiento, lugarNacimiento):
    p = {}
    p['nombre'] = nombre
    p['fecha'] = fechaNacimiento
    p['lugar'] = lugarNacimiento
    return p

cliente = MongoClient()

db = cliente['pymongodb']

personas = db['personas']

# persona1 = {
#     'nombre': 'Pedro',
#     'fecha': '1985/11/04',
#     'lugar': 'Sonora'
# }
#
# persona2 = {
#     'nombre': 'Jose',
#     'fecha': '1985/11/04',
#     'lugar': 'Sonora'
# }
#
# persona3 = {
#     'nombre': 'Juan',
#     'apellido': 'Valenzuela',
#     'edad': 34
# }
#
# persona4 = persona('Ana', '2000/02/23', 'Jalisco')
# print(persona4)

nombres = ['ana', 'maria', 'jose']
fechas = ['2000/02/23', '1952/08/12', '1997/12/07']
lugares = ['Jalisco', 'Colima', 'Nayarit']

lista_personas = []

for n, f, l in zip(nombres, fechas, lugares):
    lista_personas.append(persona(n, f, l))

# for p in lista_personas:
#     personas.insert_one(p)

result = personas.insert_many(lista_personas)
print(result.inserted_ids)
pass

#
# result = personas.insert_one(persona3)
# print(f'Persona: {result.inserted_id}')
#
# result2 = personas.insert_many([persona, persona])
# print(f'Personas: {result2.inserted_ids}')

# filtro = personas.find_({'nombre': 'Pedro'})
#
# for p in filtro:
#     print(p)
#     # print(p['apellido'])
#
# pass