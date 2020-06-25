import socket as s
import time
from threading import Thread



def enviar(sock, saddr):
    pktCount = 0

    while True:
        msg = f'Mensaje {pktCount+1} de cliente UDP'
        bytes = msg.encode()
        sock.sendto(bytes, saddr)
        print(f'[SND] Paquete {pktCount+1} enviado a {addr}')
        pktCount += 1
        time.sleep(1)


def recibir(sock):
    pktCount = 0

    while True:
        data, addr = sock.recvfrom(1024)
        print(f'[RCV] Recibido [{pktCount+1}]: {data} de {addr}')

        pktCount += 1


cliente = s.socket(s.AF_INET, s.SOCK_DGRAM)


ip = '127.0.0.1'
port = 12345

addr = ip, port


# Iniciar thread de envio
e = Thread(target=enviar, args=(cliente, addr))

time.sleep(3)

# Iniciar thread de recepcion
r = Thread(target=recibir, args=(cliente, ))

e.start()
r.start()



