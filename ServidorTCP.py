import socket as s

serverSocket = s.socket()
print('Se ha creado el socket del servidor')

ip = '127.0.0.1'
port = 35491

serverSocket.bind((ip, port))
print(f'El socket del servidor esta atado a la direccion ip {ip} y el puerto {port}')


serverSocket.listen()

contador = 0

while True:
    if contador < 10:
        (clienteCon, clientAddr) = serverSocket.accept()
        print(f'Tipo de clienteCon: {type(clienteCon)}')
        print(f'Tipo de clientAddr: {type(clientAddr)}')
        print(f'addr: {clientAddr}')
    else:
        continue

    contador += 1

    print(f'Conexion {contador} aceptada de {clientAddr}')

    while True:
        data = clienteCon.recv(1024)
        print(f'data: {type(data)}')

        print(data)

        if data != b'':
            msg1 = 'Mensaje recibido'
            msg1Bytes = msg1.encode()  # str.encode(msg1)

            msg2 = 'Se va a cerrar la conexion'
            msg2Bytes = msg2.encode()

            clienteCon.send(msg1Bytes)
            clienteCon.send(msg2Bytes)

            print('Conexion cerrada')
            clienteCon.close()

            contador -= 1

            break