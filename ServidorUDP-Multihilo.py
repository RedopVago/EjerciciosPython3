import socket as s
import time
from threading import Thread


def recibir(sock):
    pktCount = 0
    isSending = False

    while True:
        data, addr = sock.recvfrom(1024)

        if not isSending:
            # Iniciar thread de envio
            e = Thread(target=enviar, args=(sock, addr))
            e.start()

            isSending = True

        pktCount += 1
        print(f'[RCV {pktCount}] Recibi un mensaje: {data} de {addr}')


def enviar(sock, caddr):

    pktCount = 0

    while True:
        if caddr:
            msg = f'Hola {pktCount+1}'
            sock.sendto(msg.encode(), caddr)
            print(f'[SND] Paquete {pktCount+1} enviado a {caddr}')
            pktCount += 1
        else:
            print(f'[SND-ERROR]caddr es {caddr}')

        time.sleep(0.5)


socketServidor = s.socket(s.AF_INET, s.SOCK_DGRAM)
print('Se ha creado el socket del servidor')

ip = ''
port = 12345

socketServidor.bind((ip, port))
print(f'El socket del servidor esta atado a la direccion ip {ip} y el puerto {port}')

# Iniciar thread de recepcion
r = Thread(target=recibir, args=(socketServidor,))

r.start()
