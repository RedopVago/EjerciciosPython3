import socket as s

socketServidor = s.socket(s.AF_INET, s.SOCK_DGRAM)
print('Se ha creado el socket del servidor')

ip = ''
port = 12345

socketServidor.bind((ip, port))
print(f'El socket del servidor esta atado a la direccion ip {ip} y el puerto {port}')

salir = False

pktCount = 0

print('Esperando paquetes')

while not salir:
    data, addr = socketServidor.recvfrom(1024)

    pktCount += 1
    print(f'[{pktCount}] Recibi un mensaje: {data} de {addr}')

    msg = 'Mensaje recibido!'
    socketServidor.sendto(msg.encode(), addr)

