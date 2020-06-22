import socket as s

cliente = s.socket()

cliente.connect(('127.0.0.1', 35491))
print(f'Conectado al servidor')

msg = 'Hola'
bytes = msg.encode()

cliente.send(bytes)


while True:

    data = cliente.recv(1024)
    print(data)

    if data == b'':
        print('Conexion se termino')
        break

cliente.close()
