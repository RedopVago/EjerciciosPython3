import socket as s

import time

cliente = s.socket()

cliente.connect(('127.0.0.1', 35491))
print(f'Conectado al servidor')

salir = False

while not salir:
    msg = 'Mensaje de cliente TCP'
    bytes = msg.encode()

    cliente.send(bytes)

    data = cliente.recv(1024)

    print(f'Recibido: {data}')

    time.sleep(2)

cliente.close()
