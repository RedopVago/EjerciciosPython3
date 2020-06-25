import socket as s

serverSocket = s.socket()
print('Se ha creado el socket del servidor')

ip = ''
port = 35491

serverSocket.bind((ip, port))
print(f'El socket del servidor esta atado a la direccion ip {ip} y el puerto {port}')


serverSocket.listen()

salir = False

pktCount = 0

while not salir:
    (clienteCon, clientAddr) = serverSocket.accept()

    pktCount += 1

    print('Esperando paquetes')

    while True:
        data = clienteCon.recv(1024)

        pktCount += 1
        print(f'[{pktCount}] Recibi un mensaje: {data} de {clientAddr}')

        msg = 'Mensaje recibido!'

        clienteCon.send(msg.encode())

    print('Conexion cerrada')
    clienteCon.close()