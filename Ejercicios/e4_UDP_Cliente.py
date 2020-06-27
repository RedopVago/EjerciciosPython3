import socket as s


class ClienteUDP:

    __sock = None

    __sndPktCount = 0
    __rcvPktCount = 0

    def __init__(self, ip, puerto):
        self.__sock = s.socket()
        self.__sock.connect((ip, puerto))

        salir = False

        while not salir:
            print('Escribe un mensaje (Quit para salir):')
            tmp = input()

            self.enviar(tmp.encode(), (ip, puerto))

            rcv = self.recibir()
            print(f'[RCV: {self.__rcvPktCount}] {rcv}')

            if tmp == 'Quit':
                salir = True
                print('Saliendo ...')
                continue

    def enviar(self, mensaje, addr):
        self.__sndPktCount += 1
        print(f'[SND:{self.__sndPktCount}] {mensaje}')
        self.__sock.send(mensaje.encode(), addr)

    def recibir(self):
        data, addr = self.__sock.recv(1024)
        self.__rcvPktCount += 1
        return data.decode(), addr
