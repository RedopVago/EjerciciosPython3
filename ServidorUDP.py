import socket as s

socketServidor = s.socket(s.AF_INET, s.SOCK_DGRAM)
type(socketServidor)

ip = '127.0.0.1'
port = 12345

socketServidor.bind((ip, port))

salir = False

while not salir:
    print('Esperando paquetes')
    data, addr = socketServidor.recvfrom(1024)
    print(f'Recibi un mensaje: {data} de {addr}')

    msg = 'Mensaje recibido!'
    socketServidor.sendto(msg.encode(), addr)
