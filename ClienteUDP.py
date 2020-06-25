import socket as s

import time

cliente = s.socket(s.AF_INET, s.SOCK_DGRAM)


ip = '127.0.0.1'
port = 12345

addr = ip, port

salir = False

while not salir:
    msg = 'Mensaje de cliente UDP'
    bytes = msg.encode()

    cliente.sendto(bytes, addr)

    data, addr = cliente.recvfrom(1024)

    print(f'Recibido: {data} de {addr}')

    time.sleep(2)



